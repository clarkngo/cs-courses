import requests
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor
import mlflow
from mlflow.models import infer_signature
from dotenv import load_dotenv
import os
import numpy as np

# Get ExpressJS server URL from environment variables
EXPRESSJS_URL = "http://127.0.0.1:3000"

# Fetch data from ExpressJS server
response = requests.get(f"{EXPRESSJS_URL}/movies")
data = response.json()
transformed_data = [{'genres': item['genres'], 'imdb': {'rating': item['imdb']['rating']}} for item in data]

# Convert data to DataFrame
df = pd.DataFrame(transformed_data)
print(df)

# Inspect the genres column
print("Sample values from genres column:")
print(df['genres'].head(10))
print("Data type of genres column:", df['genres'].dtype)

# Process genres
def process_genres(value):
    if isinstance(value, dict):
        return value.get('genres', [])
    elif isinstance(value, str):
        return value.split(',')
    elif isinstance(value, list):
        return value
    else:
        return []

df['genres'] = df['genres'].apply(process_genres)

# Remove rows with empty genres lists
df = df[df['genres'].apply(lambda x: len(x) > 0)]

# One-hot encode genres
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df['genres'])

# Extract IMDb rating
def extract_imdb_rating(imdb_info):
    if isinstance(imdb_info, dict):
        rating = imdb_info.get('rating', None)
        if isinstance(rating, str):
            try:
                return float(rating)
            except ValueError:
                return np.nan
        elif isinstance(rating, (float, int)):
            return float(rating)
    return np.nan

df['imdb_rating'] = df['imdb'].apply(extract_imdb_rating)
df['imdb_rating'] = df['imdb_rating'].fillna(df['imdb_rating'].mean())

# Define features and labels
y = df['imdb_rating']

# Check if X and y have the same length
if len(X) != len(y):
    raise ValueError("Length of features and labels do not match.")

# Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the Gradient Boosting model
gbr = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbr.fit(X_train, y_train)

# Predict on the test set
y_pred = gbr.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Logging with MLflow
mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("Movie Genre Prediction")

with mlflow.start_run():
    # Log hyperparameters
    mlflow.log_params({
        "n_estimators": 100,
        "learning_rate": 0.1,
        "max_depth": 3
    })

    # Log metrics
    mlflow.log_metrics({
        "mean_squared_error": mse,
        "r2_score": r2
    })

    # Log model
    signature = infer_signature(X_train, gbr.predict(X_train))
    model_info = mlflow.sklearn.log_model(
        sk_model=gbr,
        artifact_path="movie_genre_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="MovieGenreGBModel"
    )

    # Log data schema and additional tags
    mlflow.set_tag("Data Schema", mlb.classes_)
    mlflow.set_tag("Model Type", "Gradient Boosting")

# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
predictions = loaded_model.predict(X_test)

# Display some predictions
result = pd.DataFrame(predictions, columns=["predicted_rating"])
print(result.head())
