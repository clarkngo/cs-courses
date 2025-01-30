import React, { Component } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { LogBox } from 'react-native';

LogBox.ignoreLogs([
  'Non-serializable values were found in the navigation state',
]);

import Cities from '../../src/Cities/Cities'
import AddCity from '../../src/AddCity/AddCity'


const Tab = createBottomTabNavigator();

export default class App extends Component {
  state = {
    cities: []
  }

  addCity = (city) => {
    const cities = this.state.cities
    cities.push(city)
    this.setState({ cities })
  }

  render() {
    return (
      <NavigationContainer>
        <Tab.Navigator>
          <Tab.Screen name="Cities"  initialParams={{cities: this.state.cities, addCity: this.addCity}} component={Cities} />
          <Tab.Screen name="AddCity" initialParams={{cities: this.state.cities, addCity: this.addCity}} component={AddCity} />
        </Tab.Navigator>
      </NavigationContainer>
    );
  }
}