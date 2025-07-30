[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/3aWwWlXX)
# DIT637-TT04
test trigger
# How to Run If Setup has been done

## Backend - ExpressJS
In a new terminal type: 
- `cd backend-expressjs`
- `npm install` 
- `npm run start`

## Frontend - React Native
In a new terminal type: 
- `cd frontend-reactnative`
- `npm install`
- `npx expo login`
- `npx expo start --tunnel`
5. Scan the QR Code with your mobile phone

# Setup
## Database - MongoDB Atlas
1. Create an account
2. Create DB copy MongoDB connection string

## Backend - ExpressJS
1. Go inside backend-expressjs folder create `.env` 
2. Follow the `example.env` file and paste the MongoDB connection string
3. In a new terminal type: 
- `cd backend-expressjs`
- `npm install` 
- `npm run start`
- make sure its allowed public access.
4. Copy the forwarded address

## Frontend - React Native
1. Create an Expo Go account and download in your Mobile Phone
2. Go inside frontend-reactnative folder create `.env` 
3. Follow the `example.env` file and paste the forwarded address of backend server
4. In a new terminal type: 
- `cd frontend-reactnative`
- `npm install`
- `npx expo login`
- `npx expo start --tunnel`
5. Scan the QR Code with your mobile phone

After completing these steps, you should be able to test your mobile app
