# 01-module

---

# Project Overview

## Setup Instructions

### 1. **Backend Setup:**
1. **Create a `.env` file** in the **backend/** directory to store your MongoDB URI and port configuration. You can copy the format from `example.env`:
   ```bash
   MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/sample_supplies?retryWrites=true&w=majority
   PORT=5000
   ```

2. **Start MongoDB Atlas** and ensure the connection is correct by configuring the connection string in your `.env` file.

3. **Install dependencies** and run the backend:
   ```bash
   cd backend
   npm install
   npx ts-node src/app.ts
   ```

4. **Test the backend**: Verify the `api/hello` route using Postman or your browser:
   ```
   http://localhost:5000/api/hello
   ```

### 2. **Frontend Setup:**
1. **Create a `.env` file** in the **frontend/** directory to store the API URL. You can copy the format from `example.env`:
   ```bash
   REACT_APP_API_URL=http://localhost:5000/api
   ```

2. **Install frontend dependencies** and run the frontend:
   ```bash
   cd frontend
   npm install
   npm start
   ```

3. **Visit the frontend**: Open `http://localhost:3000` in your browser to see the React app displaying data fetched from the backend and MongoDB Atlas.

---

## Expected Output:
The React frontend will display a **"Hello from MongoDB!"** message along with a sample sales record from the **sample_supplies.sales** collection in MongoDB Atlas.

---

## 1. **Frontend (React + Axios + TypeScript)**

The frontend is built using **React**, a JavaScript library for building user interfaces. In this project, React is combined with **TypeScript**, which adds type safety to the code, reducing errors and making it easier to manage large-scale applications.

### Key Components:
- **App.tsx**: 
  - The main entry point of the React application.
  - Written in TypeScript (`.tsx` extension), which allows you to define types for the props, state, and other components.
  - Calls a service layer function to fetch data from the backend and displays the results.
  
```typescript
import React, { useEffect, useState } from 'react';
import { fetchHelloWorld } from './services/api';

const App: React.FC = () => {
  const [message, setMessage] = useState<string>('');
  const [sampleSale, setSampleSale] = useState<any>(null);

  useEffect(() => {
    async function fetchData() {
      try {
        const data = await fetchHelloWorld();
        setMessage(data.message);
        setSampleSale(data.sampleSale);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    fetchData();
  }, []);

  return (
    <div>
      <h1>{message}</h1>
      {sampleSale && (
        <div>
          <h2>Sample Sale Data:</h2>
          <p><strong>Store Location:</strong> {sampleSale.storeLocation}</p>
          <p><strong>Sale Date:</strong> {new Date(sampleSale.saleDate).toLocaleDateString()}</p>
          <p><strong>Items:</strong> {sampleSale.items.length}</p>
        </div>
      )}
    </div>
  );
};

export default App;
```

- **api.ts**:
  - Service layer that uses **Axios** to make HTTP requests to the backend API.
  - Axios simplifies making requests and handling responses.
  - The `api.ts` file is also written in TypeScript, making the function signatures explicit and ensuring that data types (e.g., response data) are clearly defined.

```typescript
import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const fetchHelloWorld = async () => {
  const response = await axios.get(`${API_URL}/hello`);
  return response.data;
};
```

---

## 2. **Backend (Express + MongoDB Atlas + TypeScript)**

The backend is built with **Node.js** using the **Express** framework. The backend is responsible for handling HTTP requests, querying the database (MongoDB Atlas), and returning the data to the frontend.

### Key Components:
- **app.ts**:
  - The main file that sets up the Express server and middleware.
  - Configures CORS to allow requests from the frontend.
  - Manages the connection to **MongoDB Atlas** using **Mongoose** and listens for incoming API requests.

```typescript
import express from 'express';
import mongoose from 'mongoose';
import cors from 'cors';
import dotenv from 'dotenv';
import routes from './routes';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Enable CORS for all routes
app.use(cors());

// Middleware
app.use(express.json());
app.use('/api', routes);

// MongoDB Connection
mongoose.connect(process.env.MONGODB_URI!)
  .then(() => console.log('Connected to MongoDB'))
  .catch((error) => console.log('MongoDB connection error:', error));

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

- **routes.ts**:
  - Defines the API routes available to the frontend.
  - The `/hello` route fetches data from the `sales` collection in MongoDB Atlas and sends it to the frontend.
  - Written in TypeScript, making it easier to manage request and response types.

```typescript
import { Router, Request, Response } from 'express';
import mongoose from 'mongoose';

const router = Router();

const saleSchema = new mongoose.Schema({
  saleDate: Date,
  items: Array,
  storeLocation: String,
  customer: Object,
}, { collection: 'sales' });

const Sale = mongoose.model('Sale', saleSchema);

router.get('/hello', async (req: Request, res: Response) => {
  try {
    const sales = await Sale.findOne();
    if (sales) {
      res.json({
        message: 'Hello from MongoDB!',
        sampleSale: sales,
      });
    } else {
      res.json({ message: 'No data found in the sales collection' });
    }
  } catch (error) {
    res.status(500).json({ message: 'Error fetching data from MongoDB', error });
  }
});

export default router;
```

---

## 3. **JavaScript vs. TypeScript**

### **JavaScript**:
- **JavaScript** is a dynamic, loosely typed language and is widely used for both frontend and backend development.
- While JavaScript allows for rapid prototyping, its dynamic nature means that errors can go unnoticed until runtime, leading to potential bugs.

### **TypeScript**:
- **TypeScript** is a superset of JavaScript that adds static typing. This means that you can explicitly define the types of variables, functions, and components.
- TypeScript enhances the developer experience by providing **compile-time error checking**, **code autocompletion**, and **type safety**.
- In this project, **TypeScript** is used for both the frontend and backend, improving the maintainability and scalability of the codebase.
  
### **Advantages of TypeScript in This Project**:
1. **Type Safety**: Helps catch errors early, especially in API calls, by enforcing consistent types between the frontend and backend.
2. **Enhanced Developer Experience**: Better tooling and autocompletion in IDEs, reducing development time and improving code quality.
3. **Clearer Code**: Types make it easier to understand how data flows through the application, especially in large codebases.
4. **Less Runtime Errors**: Many errors that would only appear at runtime in JavaScript are caught during development with TypeScript.

---
