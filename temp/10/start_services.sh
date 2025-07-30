#!/bin/bash

# Start mlflow server
cd /workspaces/DIT637-TT08/mlops-mlflow
mlflow server &
echo "mlflow server started."

# Start ExpressJS backend
cd /workspaces/DIT637-TT08/backend-expressjs
npm run start &
echo "ExpressJS backend started."

# Start FastAPI server
cd /workspaces/DIT637-TT08/modelserver-fastapi
uvicorn main:app --reload &
echo "FastAPI server started."

# Start React frontend with Expo
# cd /workspaces/DIT637-TT08/frontend-reactnative
# npx expo start --web &
# echo "React frontend with Expo started."

# Start Ollama service
cd /workspaces/DIT637-TT08/
ollama serve &
echo "Ollama service started."

# Wait for all background processes to finish
wait
