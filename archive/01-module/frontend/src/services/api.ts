import axios from 'axios';

// Use the environment variable
const API_URL = process.env.REACT_APP_API_URL;

export const fetchHelloWorld = async () => {
  const response = await axios.get(`${API_URL}/hello`);
  return response.data;
};
