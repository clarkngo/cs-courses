import { createContext, useContext, useState } from 'react';

const CityContext = createContext();

export function CityProvider({ children }) {
  const [cities, setCities] = useState([]);

  const addCity = (city) => {
    setCities((prevCities) => [...prevCities, city]);
  };

  return (
    <CityContext.Provider value={{ cities, addCity }}>
      {children}
    </CityContext.Provider>
  );
}

export function useCity() {
  return useContext(CityContext);
}
