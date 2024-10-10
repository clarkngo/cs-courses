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

4. **Find the GitHub Codespaces Forwarded Address**: 
   After running the backend, GitHub Codespaces will generate a **forwarded URL** for your backend. The URL will look something like this:
   ```
   https://animated-succotash-wv6pq9rrgpx35rr9-5000.app.github.dev
   ```

5. **Test the backend**: Verify the `api/hello` route using Postman or your browser:
   ```
   https://animated-succotash-wv6pq9rrgpx35rr9-5000.app.github.dev/api/hello
   ```

### 2. **Frontend Setup:**
1. **Create a `.env` file** in the **frontend/** directory to store the API URL. Replace `localhost` with the **GitHub Codespaces forwarded address** for the backend API:
   ```bash
   REACT_APP_API_URL=https://animated-succotash-wv6pq9rrgpx35rr9-5000.app.github.dev/api
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

### Example `.env` files

#### **Backend `.env`**:

```bash
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/sample_supplies?retryWrites=true&w=majority
PORT=5000
```

#### **Frontend `.env`**:

```bash
REACT_APP_API_URL=https://animated-succotash-wv6pq9rrgpx35rr9-5000.app.github.dev/api
```

---
