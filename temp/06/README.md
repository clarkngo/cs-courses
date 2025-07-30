[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/njX8kneg)
# DIT637-TT06 

## Run Backend ExpressJS DB server
1. Copy your MongoDB Connection String from MongoDB Atlas
2. Create `.env` file and paste it after `MONGODB_URI=`
3. Open New Terminal
4. `cd backend-expressjs`
5. `npm install`
7. `npm run start`
8. Make the Port Visibility `Public`
9. Copy the forwarded address ExpressJS

## Run Backend FastAPI recommendation server
1. Create `.env` file and paste the forwarded address ExpressJS after `EXPRESSJS_BASE_URL=`
2. Open New Terminal
3. `cd backend-fastapi`
4. `pip install -r requirements.txt`
5. `uvicorn main:app --host 0.0.0.0 --port 8000`
6. Make the Port Visibility `Public`
7. Copy the forwarded address FastAPI

## Run Frontend React Native in the Mobile/Browser
1. Create `.env` file and paste the following:
- paste the forwarded address ExpressJS after  `API_URL_SEARCH=`
- paste the forwarded address FastAPI after `API_URL_RECOMMEND=`
2. Open New Terminal
3. `cd frontend-reactnative`
4. `npm install`
5. `npx expo login`
6. `npx expo start --tunnel` OR in the web `npx expo start --web`
