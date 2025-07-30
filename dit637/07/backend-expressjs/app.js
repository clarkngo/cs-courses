import express from 'express';
import mongoose from 'mongoose';
import dotenv from 'dotenv';
import cors from 'cors';
import bodyParser from 'body-parser'; 
import morgan from 'morgan';

dotenv.config();

const app = express();
const port = 3000;

app.use(cors()); // Enable CORS
app.use(bodyParser.json()); // Middleware to parse JSON request bodies
app.use(morgan('dev')); // Log HTTP requests

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

const isValidObjectId = (id) => {
  return mongoose.Types.ObjectId.isValid(id) && (String(new mongoose.Types.ObjectId(id)) === id);
};

const getRandomElements = (array, count) => {
  const shuffled = array.sort(() => 0.5 - Math.random());
  return shuffled.slice(0, count);
};

function getProjection(fields) {
  if (fields === 'all') {
      return {}; // Return all fields
  } else {
      return {
          title: 1,
          genres: 1,
          'imdb.rating': 1,
          cast: 1
      };
  }
}

app.get('/movies', connectToMongoDB, async (req, res) => {
  try {
      const { page = 1, limit = 500, fields = 'basic' } = req.query; // Default to page 1 and 500 items per page
      const projection = getProjection(fields);
      const movies = await Movie.find({}, projection)
                                .skip((page - 1) * limit)
                                .limit(parseInt(limit));
      res.json(movies);
  } catch (error) {
      console.error('Error retrieving movies:', error);
      res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.post('/movies', connectToMongoDB, async (req, res) => {
  const { movie_ids, fields = 'basic' } = req.body;

  try {
      if (!Array.isArray(movie_ids)) {
          return res.status(400).json({ error: 'Invalid input, expected an array of movie IDs' });
      }
      
      // Validate and convert movie IDs to ObjectId format
      const validObjectIds = movie_ids.filter(id => isValidObjectId(id))
                                      .map(id => new mongoose.Types.ObjectId(id));
      
      if (validObjectIds.length === 0) {
          return res.status(400).json({ error: 'No valid movie IDs provided' });
      }

      // Get projection based on fields
      const projection = getProjection(fields);
      const movies = await Movie.find({ _id: { $in: validObjectIds } }, projection);
      res.json(movies);
  } catch (error) {
      console.error('Error retrieving movie details:', error);
      res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.get('/initial-recommendations', connectToMongoDB, async (req, res) => {
  try {
      const { fields = 'basic' } = req.query; // Get fields query parameter

      // Fetch distinct genres
      const genres = await Movie.distinct('genres');
      
      if (genres.length === 0) {
          return res.status(404).json({ error: 'No genres found' });
      }

      // Randomly select 5 genres
      const selectedGenres = getRandomElements(genres, 5);

      // Get projection based on fields
      const projection = getProjection(fields);

      // Fetch 5 movies for each selected genre
      const recommendations = await Promise.all(selectedGenres.map(async (genre) => {
          const movies = await Movie.find({ genres: genre }, projection).limit(5);
          return {
              genre,
              movies
          };
      }));

      res.json(recommendations);
  } catch (error) {
      console.error('Error retrieving initial recommendations:', error);
      res.status(500).json({ error: 'Internal Server Error' });
  }
});

app.post('/similar', connectToMongoDB, async (req, res) => {
    const { genres, cast } = req.body;

    try {
        // Fetch similar movies based on cast
        const similarActors = await Movie.find({ cast: { $in: cast } }).limit(10);
        // Fetch similar movies based on genres
        const similarGenres = await Movie.find({ genres: { $in: genres } }).limit(10);

        res.json({
            actors: similarActors,
            genres: similarGenres
        });
    } catch (error) {
        console.error('Error retrieving recommendations:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

// Health check endpoint with JSON response
app.get('/', (req, res) => {
    res.json({ message: 'Express.js server is running' });
});

if (process.env.NODE_ENV !== 'test') {
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}

// Export the app for testing
export default app;
