from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
from mlflow.models import infer_signature
from dotenv import load_dotenv
import os
import numpy as np

# Load environment variables from .env file
load_dotenv()

# Get MongoDB details from environment variables
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

client = MongoClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Fetch data from MongoDB
data = list(collection.find({}, {'_id': 0, 'genres': 1, 'imdb.rating': 1}))
df = pd.DataFrame(data)

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

# Verify processed genres
print("Data type of genres column after processing:", type(df['genres'].iloc[0]))
print("First few rows of genres after processing:", df['genres'].head())

# Remove rows with empty genres lists
df = df[df['genres'].apply(lambda x: len(x) > 0)]

# One-hot encode genres
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(df['genres'])
print("Classes found by MultiLabelBinarizer:", mlb.classes_)
print("Shape of X after encoding:", X.shape)

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

print("Length of X:", len(X))
print("Length of y:", len(y))

# Model Training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train the Random Forest model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Predict on the test set
y_pred = rf.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Logging with MLflow
mlflow.set_tracking_uri("http://127.0.0.1:8080")
mlflow.set_experiment("Movie Genre Prediction")

with mlflow.start_run():
    # Log hyperparameters
    mlflow.log_params({
        "n_estimators": 100,
        "random_state": 42
    })

    # Log metrics
    mlflow.log_metrics({
        "mean_squared_error": mse,
        "r2_score": r2
    })

    # Log model
    signature = infer_signature(X_train, rf.predict(X_train))
    model_info = mlflow.sklearn.log_model(
        sk_model=rf,
        artifact_path="movie_genre_rf_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="MovieGenreRFModel"
    )

    # Log data schema and additional tags
    mlflow.set_tag("Data Schema", mlb.classes_)
    mlflow.set_tag("Model Type", "Random Forest")

# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)
predictions = loaded_model.predict(X_test)

# Display some predictions
result = pd.DataFrame(predictions, columns=["predicted_rating"])
print(result.head())

# Additional Cleanup
client.close()
