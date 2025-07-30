import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';
import cors from 'cors';

dotenv.config();

const app = express();
const port = 3000;

// Enable CORS
app.use(cors());

const uri = process.env.MONGODB_URI;
if (!uri) {
    console.error('MongoDB URI is not defined');
    process.exit(1);
}

let isConnected = false;

// Middleware to connect to MongoDB on demand
const connectToMongoDB = async (req, res, next) => {
  if (!isConnected) {
    try {
      await mongoose.connect(uri, {
        dbName: 'sample_mflix' // Set the database name
      });
      isConnected = true;
      console.log('Connected to MongoDB Atlas');
    } catch (error) {
      console.error('Error connecting to MongoDB Atlas:', error);
      return res.status(500).json({ error: 'Internal Server Error' });
    }
  }
  next();
};

// Define a movie schema
const movieSchema = new mongoose.Schema({
  title: String,
  genres: [String],
  cast: [String],
  year: Number
}, { collection: 'movies' }); // Set the collection name

// Create a movie model
const Movie = mongoose.model('Movie', movieSchema);

// Apply middleware to routes that need MongoDB connection
app.get('/movies', connectToMongoDB, async (req, res) => {
  try {
    const movies = await Movie.find();
    res.json(movies);
  } catch (error) {
    console.error('Error retrieving movies:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/', (req, res) => {
  res.send('Hello World!');
});

if (process.env.NODE_ENV !== 'test') {
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}

// Export the app for testing
export default app;
