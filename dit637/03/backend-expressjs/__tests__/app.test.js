import mongoose from 'mongoose';
import request from 'supertest';
import app from '../server.js';  // Adjust the path as necessary

let server;
let port;

beforeAll(async () => {
  port = Math.floor(Math.random() * (65535 - 1024) + 1024); // Use a random port between 1024 and 65535

  // Connect to MongoDB
  const uri = process.env.MONGODB_URI;
  if (!uri) {
    console.error('MongoDB URI is not defined');
    process.exit(1);
  }

  await mongoose.connect(uri, {
    dbName: 'sample_mflix'
  });

  server = app.listen(port, () => {
    console.log(`Test server running on port ${port}`);
  });
});

afterAll(async () => {
  await mongoose.connection.close();
  await new Promise(resolve => server.close(resolve));
  console.log('Test server closed');
});

describe('GET /', () => {
  it('should return 200 OK and "Hello World!"', async () => {
    const res = await request(server).get('/');
    expect(res.status).toBe(200);
    expect(res.text).toBe('Hello World!');
  });
});

describe('GET /movies', () => {
  it('should return 200 OK', async () => {
    const res = await request(server).get('/movies');
    expect(res.status).toBe(200);
  }, 10000);  // Increase timeout to 10 seconds
});
