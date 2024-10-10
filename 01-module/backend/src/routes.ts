import { Router, Request, Response } from 'express';
import mongoose from 'mongoose';
import logger from './logger';

const router = Router();

// Ensure the schema matches the structure of the documents in the 'sales' collection
const saleSchema = new mongoose.Schema({
  saleDate: Date,
  items: Array,
  storeLocation: String,
  customer: Object,
}, { collection: 'sales' }); // Explicitly refer to the 'sales' collection

// Create a Mongoose model for the 'sales' collection
const Sale = mongoose.model('Sale', saleSchema);

// Route to fetch data from the 'sales' collection
router.get('/hello', async (req: Request, res: Response) => {
  try {
    // Fetch a single sale document from the 'sales' collection
    const sales = await Sale.findOne();
    logger.info('Fetched sale:', sales); // Log the fetched sale

    if (sales) {
      res.json({
        message: 'Hello from MongoDB!',
        sampleSale: sales, // Send the sale document back to the frontend
      });
    } else {
      res.json({
        message: 'No data found in the sales collection',
      });
    }
  } catch (error) {
    logger.error('Error fetching data from MongoDB:', error);
    res.status(500).json({ message: 'Error fetching data from MongoDB', error });
  }
});

export default router;
