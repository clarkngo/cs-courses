import React, { useState } from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Cities from './cities';
import AddCity from './add-city';

const Tab = createBottomTabNavigator();

export default function TabLayout() {
  const [cities, setCities] = useState([]);

  const addCity = (city) => {
    setCities((prevCities) => [...prevCities, city]);
  };

  return (
    <Tab.Navigator>
      <Tab.Screen name="cities">
        {(props) => <Cities {...props} cities={cities} />}
      </Tab.Screen>
      <Tab.Screen name="add-city">
        {(props) => <AddCity {...props} addCity={addCity} />}
      </Tab.Screen>
    </Tab.Navigator>
  );
}
