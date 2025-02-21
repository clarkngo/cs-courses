import React, { Component } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { LogBox } from 'react-native';

LogBox.ignoreLogs([
  'Non-serializable values were found in the navigation state',
]);

import Cities from './src/Cities/Cities';
import City from './src/Cities/City';
import AddCity from './src/AddCity/AddCity';
import { colors } from './src/theme';

const Tab = createBottomTabNavigator();
const Stack = createNativeStackNavigator();

function CitiesStackScreen({ navigation, route, cities, addCity, addLocation }) {
  return (
    <Stack.Navigator
      screenOptions={{
        headerStyle: {
          backgroundColor: colors.primary,
        },
        headerTintColor: '#fff',
      }}
    >
      <Stack.Screen
        name="Cities"
        children={(props) => (
          <Cities {...props} cities={cities} addCity={addCity} addLocation={addLocation} />
        )}
      />
      <Stack.Screen
        name="City"
        children={(props) => (
          <City {...props} cities={cities} addCity={addCity} addLocation={addLocation} />
        )}
      />
    </Stack.Navigator>
  );
}

export default class App extends Component {
  state = {
    cities: [],
  };

  addCity = (city) => {
    this.setState((prevState) => ({
      cities: [...prevState.cities, { ...city, locations: [] }],
    }));
  };

  addLocation = (location, city) => {
    const index = this.state.cities.findIndex((item) => item.id === city.id);
    const updatedCity = { ...this.state.cities[index], locations: [...this.state.cities[index].locations, location] };

    const cities = [
      ...this.state.cities.slice(0, index),
      updatedCity,
      ...this.state.cities.slice(index + 1),
    ];

    this.setState({ cities });
  };

  render() {
    return (
      <NavigationContainer>
        <Tab.Navigator>
          <Tab.Screen
            name="Cities"
            children={(props) => (
              <CitiesStackScreen
                {...props}
                cities={this.state.cities}
                addCity={this.addCity}
                addLocation={this.addLocation}
              />
            )}
          />
          <Tab.Screen
            name="AddCity"
            children={(props) => (
              <AddCity
                {...props}
                cities={this.state.cities}
                addCity={this.addCity}
                addLocation={this.addLocation}
              />
            )}
          />
        </Tab.Navigator>
      </NavigationContainer>
    );
  }
}
