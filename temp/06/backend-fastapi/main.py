from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from typing import List
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's URL in production
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

# Unified function to fetch movie details or similar movies
def fetch_movie_data(movie_ids: List[str] = None, genres: List[str] = None, cast: List[str] = None):
    try:
        expressjs_base_url = os.getenv("EXPRESSJS_BASE_URL")
        if not expressjs_base_url:
            raise ValueError("Express.js base URL is not set in environment variables")

        if movie_ids:
            url = f"{expressjs_base_url}/movies"
            payload = {"movie_ids": movie_ids}
        elif genres and cast:
            url = f"{expressjs_base_url}/similar"
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

# Helper function to fetch all movies for similarity comparison
def fetch_all_movies():
    try:
        expressjs_base_url = os.getenv("EXPRESSJS_BASE_URL")
        if not expressjs_base_url:
            raise ValueError("Express.js base URL is not set in environment variables")

        url = f"{expressjs_base_url}/movies"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching all movies from Express.js: {e}")
        return None
    except ValueError as e:
        print(e)
        return None

# Helper function to compute similarity
def compute_similarity(selected_movies, all_movies):
    def create_features(movie):
        return " ".join(movie['genres'] + movie['cast'])

    selected_features = [create_features(movie) for movie in selected_movies]
    all_features = [create_features(movie) for movie in all_movies]

    vectorizer = CountVectorizer().fit(all_features)
    selected_vectors = vectorizer.transform(selected_features)
    all_vectors = vectorizer.transform(all_features)

    similarity_scores = cosine_similarity(selected_vectors, all_vectors)
    return similarity_scores.mean(axis=0)

@app.post("/recommend")
async def recommend(request: MovieIdsRequest):
    movie_ids = request.movieIds

    selected_movies = fetch_movie_data(movie_ids=movie_ids)
    if not selected_movies:
        raise HTTPException(status_code=500, detail="Error fetching movie details")

    all_movies = fetch_all_movies()
    if not all_movies:
        raise HTTPException(status_code=500, detail="Error fetching all movies")

    similarity_scores = compute_similarity(selected_movies, all_movies)

    selected_movie_titles = {movie['title'] for movie in selected_movies}
    sorted_indices = np.argsort(similarity_scores)[::-1]
    recommendations = [
        all_movies[i] for i in sorted_indices if all_movies[i]['title'] not in selected_movie_titles
    ][:3]  # Top 3 recommendations

    return {"recommendations": recommendations}

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

# Test endpoint for health check
@app.get('/')
def read_root():
    return {"message": "FastAPI is running"}
