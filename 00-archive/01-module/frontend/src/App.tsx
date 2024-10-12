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
