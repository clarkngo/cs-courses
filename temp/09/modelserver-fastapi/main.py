from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import requests
from typing import List
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import CountVectorizer
import mlflow.pyfunc
import logging
import math
import asyncio
import httpx
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from langchain_community.embeddings.ollama import OllamaEmbeddings

EXPRESSJS_URL = "http://127.0.0.1:3000"
OLLAMA_URL = "http://127.0.0.1:11434"
MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"

# Configure logging
logging.basicConfig(level=logging.INFO)

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)

# Define model details
MODEL_NAME = "MovieGenreGBModel"
MODEL_VERSION = 1

# Load model from MLflow
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
model = mlflow.pyfunc.load_model(model_uri=model_uri)


CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""

# FastAPI app initialization
app = FastAPI()

class QueryRequest(BaseModel):
    query_text: str

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="gemma2:2b")
    return embeddings

def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="gemma2:2b")
    response_text = model.invoke(prompt)
    
    return response_text

app = FastAPI()

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request models
class MovieIdsRequest(BaseModel):
    movieIds: List[str]

class SimilarRequest(BaseModel):
    genres: List[str]
    cast: List[str]
    title: str 

class GenerateRequest(BaseModel):
    model: str
    prompt: str

# Unified function to fetch movie details or similar movies
def fetch_movie_data(movie_ids: List[str] = None, genres: List[str] = None, cast: List[str] = None):
    try:
        if movie_ids:
            url = f"{EXPRESSJS_URL}/movies"
            payload = {"movie_ids": movie_ids}
        elif genres and cast:
            url = f"{EXPRESSJS_URL}/similar"
            payload = {"genres": genres, "cast": cast}
        else:
            raise ValueError("Insufficient parameters provided for request")

        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data from Express.js: {e}")
        return None
    except ValueError as e:
        print(e)
        return None

def fetch_movies():
    url = f"{EXPRESSJS_URL}/movies"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

# Functions for processing and transforming data
def genre_names_to_vector(genres, num_genres=23):
    genre_vector = [0] * num_genres
    genre_indices = {
        'Action': 0, 'Adventure': 1, 'Animation': 2, 'Biography': 3,
        'Comedy': 4, 'Crime': 5, 'Documentary': 6, 'Drama': 7, 'Family': 8,
        'Fantasy': 9, 'FilmNoir': 10, 'History': 11, 'Horror': 12, 'Music': 13,
        'Musical': 14, 'Mystery': 15, 'Romance': 16, 'SciFi': 17, 'Short': 18,
        'Sport': 19, 'Thriller': 20, 'War': 21, 'Western': 22
    }
    for genre in genres:
        if genre in genre_indices:
            genre_vector[genre_indices[genre]] = 1
    return genre_vector

def process_movies(movies_data):
    genre_names = [
        'Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
        'Documentary', 'Drama', 'Family', 'Fantasy', 'FilmNoir', 'History',
        'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'SciFi', 'Short',
        'Sport', 'Thriller', 'War', 'Western'
    ]

    processed_data = []
    genre_vector = {genre: 0 for genre in genre_names}
    for movie in movies_data:
        for genre in movie['genres']:
            if genre in genre_vector:
                genre_vector[genre] = 1

    return genre_vector


def recommend_based_on_genres(selected_movies):
    logging.info(f"Selected Movies Combined Genres: {selected_movies}")

    try:
        selected_genre_vectors_np = np.array(list(selected_movies.values()), dtype=np.int64).reshape(1, 23)
    except Exception as e:
        logging.error(f"Error processing selected movies' genres: {e}")
        return []

    try:
        movies = fetch_movies()
    except Exception as e:
        logging.error(f"Error fetching movies: {e}")
        return []

    similar_movies = []

    for movie in movies:
        try:
            movie_genres = genre_names_to_vector(movie.get("genres", []))
            movie_genres_np = np.array(movie_genres, dtype=np.int64).reshape(1, 23)
        except Exception as e:
            logging.error(f"Error processing genres for movie {movie.get('title', 'Unknown')}: {e}")
            continue

        if np.any(movie_genres_np) and selected_genre_vectors_np.size > 0:
            try:
                predicted_rating = model.predict(movie_genres_np)[0]
            except Exception as e:
                logging.error(f"Error predicting rating for movie {movie.get('title', 'Unknown')}: {e}")
                continue

            genre_similarity_scores = []

            for selected_genre_vector in selected_genre_vectors_np:
                if np.any(selected_genre_vector):
                    try:
                        score = 1 - cosine(movie_genres_np.flatten(), selected_genre_vector.flatten())
                        genre_similarity_scores.append(score)
                    except Exception as e:
                        logging.error(f"Error computing similarity for movie {movie.get('title', 'Unknown')}: {e}")

            genre_similarity = max(genre_similarity_scores) if genre_similarity_scores else 0.0
            genre_similarity = 0.0 if math.isnan(genre_similarity) else genre_similarity

            combined_score = predicted_rating * genre_similarity

            similar_movies.append(
                {
                    "title": movie.get("title", "Unknown"),
                    "genres": movie.get("genres", []),
                    "cast": movie.get("cast", []),
                    "predicted_rating": float(predicted_rating),
                    "genre_similarity": float(genre_similarity),
                    "combined_score": float(combined_score)
                }
            )
        else:
            logging.info(f"Skipping movie with invalid genres: {movie.get('title', 'Unknown')}")

    similar_movies.sort(key=lambda x: x["combined_score"], reverse=True)

    return similar_movies

def transform_recommendations(recommendations):
    transformed_recommendations = []
    
    for movie in recommendations:
        transformed_movie = {
            "cast": movie.get('cast', []),
            "genres": movie.get('genres', []),
            "imdb": {"rating": movie.get('predicted_rating', 0)},
            "title": movie.get('title', ""),
            "_id": movie.get('id', "")
        }
        transformed_recommendations.append(transformed_movie)
    
    return {"recommendations": transformed_recommendations}

# Define API endpoints
@app.post("/recommend")
async def recommend(request: MovieIdsRequest):
    movie_ids = request.movieIds
    selected_movies = fetch_movie_data(movie_ids=movie_ids)

    if not selected_movies:
        raise HTTPException(status_code=500, detail="Error fetching movie details")

    processed_movies = process_movies(selected_movies)
    recommended_movies = recommend_based_on_genres(processed_movies)
    top_5_movies = recommended_movies[:5]

    logging.info(f"Movie Recommendations: {top_5_movies}")
    response = transform_recommendations(top_5_movies)
    return response

@app.post('/similar')
async def similar(request: SimilarRequest):
    similars = fetch_movie_data(genres=request.genres, cast=request.cast)
    if not similars:
        raise HTTPException(status_code=500, detail="Error fetching similar movies")

    filtered_recommendations = {
        "actors": [movie for movie in similars.get('actors', []) if movie['title'] != request.title],
        "genres": [movie for movie in similars.get('genres', []) if movie['title'] != request.title]
    }

    return filtered_recommendations

@app.post("/chat")
def chat_endpoint(request: QueryRequest):
    try:
        response = query_rag(request.query_text)
        return {"response": response}    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

@app.get('/')
def read_root():
    return {"message": "FastAPI is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
