[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/WuPGNpnj)
# DIT637-TT09

## Run Ollama Server
1. Open New Terminal
2. `curl -fsSL https://ollama.com/install.sh | sh`
3. `ollama serve`

## Pull and Chat with a Large Language Model (LLM) Conversational AI
1. Open New Terminal
2. `ollama pull gemma2:2b`
3. `ollama run gemma2:2b`
4. Type anything in the prompt to test
5. Press CTRL + D to Exit

## Run Backend ExpressJS DB server (Application Server)
1. Copy your MongoDB Connection String from MongoDB Atlas
2. Create `.env` file and paste it after `MONGODB_URI=` (use `example.env` as reference)
3. Open New Terminal
4. `cd backend-expressjs`
5. `npm install`
7. `npm run start`
8. Make the Port Visibility `Public`
9. Copy the forwarded address ExpressJS

## Run Machine Learning Operations (MLOps) Tracking Server
1. Open New Terminal
2. `cd mlops-mlflow`
3. `pip install -r requirements.txt`
4. `mlflow server`

## Run Machine Learning Models
1. `cd mlops-mlflow`
2. `python run_all_models.py`

Note: It will run the following Python scripts
- model_lr is Linear Regression
- model_nn is Neural Network
- model_gb is Gradient Boost
- model_rf is Random Forest

## Run Python Script to create ChromaDB and Insert Data and Run ML Model (Recommender Server)
1. Open New Terminal
2. `cd modelserver-fastapi`
3. `pip install -r requirements.txt`
4. `python populate_database.py`
5. `uvicorn main:app --reload`

## Run Frontend React Native in the Mobile/Browser
1. Copy your ExpressJS Forwarded Address
2. Create `.env` file and paste it after `API_URL=` following: (use `example.env` as reference)
2. Open New Terminal
3. `cd frontend-reactnative`
4. `npm install`
6. `npx expo start --web`

## EXTRA: Test Ollama Server using curl command
1. New Terminal
2. Copy paste the following:

### Test Generate Response
```
curl http://localhost:11434/api/generate -d '{
  "model": "gemma2:2b",
  "prompt":"Why is the sky blue?"
}'
```
## Test Chat
```
curl -X POST http://localhost:11434/api/chat \
     -H "Content-Type: application/json" \
     -d '{
           "model": "gemma2:2b",
           "messages": [
               { "role": "user", "content": "limit 50 words. please recommed horror movies" }
           ]
         }'
```

### Test ExpressJS Server wrapping Ollama Server
```
curl -X POST http://localhost:3000/chat \
     -H "Content-Type: application/json" \
     -d '{
           "model": "gemma2:2b",
           "messages": [
               { "role": "user", "content": "limit 25 words. please recommed horror movies" }
           ]
         }'
```

### Test FastAPI RAG
```
curl -X POST "http://127.0.0.1:8000/chat" \
-H "Content-Type: application/json" \
-d '{"query_text": "What are the health benefits of green tea?"}'
```

### Test ExpressJS Wrapper FastAPI RAG
```
curl -X POST "http://127.0.0.1:3000/chat" \
-H "Content-Type: application/json" \
-d '{"query_text": "What are the health benefits of green tea?"}'
```
