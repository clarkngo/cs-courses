import argparse
import os
import shutil
from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_chroma import Chroma

import requests
import pymongo

CHROMA_PATH = "chroma"

def get_embedding_function():
    embeddings = OllamaEmbeddings(model="gemma2:2b")
    return embeddings

def load_documents():
    response = requests.get('http://127.0.0.1:3000/movies-sample')
    movies = response.json() 

    documents = []
    for movie in movies:
        if 'title' in movie and 'plot' in movie:
            print(movie['title'])
            text = f"{movie['title']} {movie['plot']}"  
            documents.append(Document(page_content=text, metadata={'movie_id': movie['_id']}))

    return documents

def split_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )
    return text_splitter.split_documents(documents)

def calculate_chunk_ids(chunks):

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    chunks_with_ids = calculate_chunk_ids(chunks)

    existing_items = db.get(include=[])  # IDs included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    new_chunks = [chunk for chunk in chunks_with_ids if chunk.metadata["id"] not in existing_ids]

    if new_chunks:
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        # no db.persist() call here
        print(f"✅ Finished adding new documents: {len(new_chunks)}")
    else:
        print("✅ No new documents to add")



def clear_database():
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)

def main():
    # Check if the database should be cleared (using the --clear flag).
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Reset the database.")
    args = parser.parse_args()
    if args.reset:
        print("✨ Clearing Database")
        clear_database()

    # Create (or update) the data store.
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)

if __name__ == "__main__":
    main()