[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/AfugNlNU)
# DIT637-TT05

# How to Run If Setup has been done

## Frontend - React Native
1. In a new terminal type: 
- `cd frontend-reactnative` 
- `npm install`
- `npx expo login`
- `npx expo start --tunnel`
2. Scan the QR Code with your mobile phone

# Setup
## Database - MongoDB Atlas
1. Create an account
2. Create DB copy MongoDB connection string

## Backend Server - Amazon EC2
1. Create an account in Amazon Web Services (AWS)
2. Find EC2 Services and create an Ubuntu Free Tier t2.micro
3. Download a new Key Pair `.pem` file. Open this locally and save somewhere
4. In Security Groups, Allow Inbound:
- `Type: HTTP, Port Range: 80, Source: Anywhere, 0.0.0.0/0`
- `Custom TCP: Port Range: 3000, Source: Anywhere, 0.0.0.0/0`
5. In the new instance, copy the following and save somewhere:
- `EC2 Public IPv4 Address`
- `EC2 Public DNS`

## CI/CD - GitHub Actions
In your current GitHub repository project (this one), go to Settings then Secrets and Variables then Actions then Secrets. 
- Add the following:
- Name: `EC2_SSH_KEY` Secret: __<contents_of_your_pem_file>__
- Name: `EC2_PUBLIC_DNS` Secret: __<your_amazon_ec2_public_dns>__
- Name: `MONGODB_URI` Secret: __<your_mongodb_connection_string>__ 

## Backend - ExpressJS
- No need to run. we will use GitHub Actions CI/CD to push this code to an Amazon EC2 Server.

## Frontend - React Native
1. Create an Expo Go account and download in your Mobile Phone
2. Go inside frontend-reactnative folder create `.env` 
3. Follow the `example.env` file and paste `EC2 Public IPv4 Address`
4. In a new terminal type: 
- `cd frontend-reactnative`
- `npm install`
- `npx expo login`
- `npx expo start --tunnel`
5. Scan the QR Code with your mobile phone

After completing these steps, you should be able to test your mobile app

Test the CI/CD
