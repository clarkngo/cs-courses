import React, { useState } from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Cities from '../../src/Cities/Cities';
import AddCity from '../../src/AddCity/AddCity';

const Tab = createBottomTabNavigator();

export default function TabLayout() {
  const [cities, setCities] = useState([]);

  const addCity = (city) => {
    setCities((prevCities) => [...prevCities, city]);
  };

  return (
    <Tab.Navigator>
      <Tab.Screen name="Cities">
        {(props) => <Cities {...props} cities={cities} />}
      </Tab.Screen>
      <Tab.Screen name="AddCity">
        {(props) => <AddCity {...props} addCity={addCity} />}
      </Tab.Screen>
    </Tab.Navigator>
  );
}
