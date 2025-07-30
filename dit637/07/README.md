[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/u9usbRVh)
# DIT637-TT07

## Run Machine Learning Operations (MLOps) Tracking Server
1. Open New Terminal
2. `cd mlops-mlflow`
3. `pip install -r requirements`
4. `mlflow server --host 127.0.0.1 --port 8080`

## Run Machine Learning Models
1. Create `.env` file inside `mlops-mlfow` (use `example.env` as reference)
2. Update the `MONGODB_URI=` variable with your MongoDB connection string
3. Copy and paste both `DATABASE_NAME=sample_mflix` and `COLLECTION_NAME=movies` in .`env` file
4. Open New Terminal
5. `cd mlops-mlflow`
6. `python run_all_models.py`

Note: It will run the following Python scripts
- model_lr is Linear Regression
- model_nn is Neural Network
- model_gb is Gradient Boost
- model_rf is Random Forest

## Run Backend ExpressJS DB server (Application Server)
1. Copy your MongoDB Connection String from MongoDB Atlas
2. Create `.env` file and paste it after `MONGODB_URI=` (use `example.env` as reference)
3. Open New Terminal
4. `cd backend-expressjs`
5. `npm install`
7. `npm run start`
8. Make the Port Visibility `Public`
9. Copy the forwarded address ExpressJS

## Run Machine Learning Model Server (Recommender Server)
1. Create `.env` file and paste the forwarded address ExpressJS after `EXPRESSJS_BASE_URL=` (use `example.env` as reference)
2. Open New Terminal
3. `cd modelserver-fastapi`
4. `pip install -r requirements.txt`
5. `uvicorn main:app --reload`
6. Make the Port Visibility `Public`
7. Copy the forwarded address FastAPI

## Run Frontend React Native in the Mobile/Browser
1. Create `.env` file and paste the following: (use `example.env` as reference)
- paste the forwarded address ExpressJS after  `API_URL_SEARCH=`
- paste the forwarded address FastAPI after `API_URL_RECOMMEND=`
2. Open New Terminal
3. `cd frontend-reactnative`
4. `npm install`
5. `npx expo login`
6. `npx expo start --tunnel` OR in the web `npx expo start --web`
