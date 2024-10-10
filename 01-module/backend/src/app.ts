import express, { Request, Response } from 'express';
import mongoose from 'mongoose';
import cors from 'cors'; // Import cors
import dotenv from 'dotenv';
import routes from './routes';
import logger from './logger'; // Import the logger

dotenv.config();

const app = express();
const PORT = process.env.PORT || 5000;

// Enable CORS for all routes
app.use(cors());

app.use(express.json());
app.use('/api', routes);

// MongoDB Connection
mongoose.connect(process.env.MONGODB_URI!)
  .then(() => logger.info('Connected to MongoDB'))
  .catch((error) => logger.error('MongoDB connection error:', error));

// Example of logging middleware
app.use((req: Request, res: Response, next) => {
  logger.info(`${req.method} ${req.url}`);
  next();
});

// Start Server
app.listen(PORT, () => {
  logger.info(`Server running on port ${PORT}`);
});
