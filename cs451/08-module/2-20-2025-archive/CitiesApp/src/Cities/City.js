import React from 'react';
import { View, Text, StyleSheet, ScrollView, TextInput, TouchableOpacity } from 'react-native';
import CenterMessage from '../components/CenterMessage';
import { colors } from '../theme';

class City extends React.Component {
  state = {
    name: '',
    info: '',
  };

  onChangeText = (key, value) => {
    this.setState({ [key]: value });
  };

  addLocation = () => {
    const { addLocation, city } = this.props.route.params;
    const { name, info } = this.state;

    if (name === '' || info === '') return;

    const location = { name, info };

    addLocation(location, city);

    this.setState({ name: '', info: '' });
  };

  render() {
    const { cities, city } = this.props.route.params;

    // Derive the updated version of the city from the global cities array
    const updatedCity = cities.find((item) => item.id === city.id) || city;

    return (
      <View style={{ flex: 1 }}>
        <ScrollView contentContainerStyle={[!updatedCity.locations.length && { flex: 1 }]}>
          <View
            style={[
              styles.locationsContainer,
              !updatedCity.locations.length && { flex: 1, justifyContent: 'center' },
            ]}
          >
            {!updatedCity.locations.length && <CenterMessage message="No locations for this city!" />}
            {updatedCity.locations.map((location, index) => (
              <View key={index} style={styles.locationContainer}>
                <Text style={styles.locationName}>{location.name}</Text>
                <Text style={styles.locationInfo}>{location.info}</Text>
              </View>
            ))}
          </View>
        </ScrollView>
        <TextInput
          onChangeText={(val) => this.onChangeText('name', val)}
          placeholder="Location name"
          value={this.state.name}
          style={styles.input}
          placeholderTextColor="white"
        />
        <TextInput
          onChangeText={(val) => this.onChangeText('info', val)}
          placeholder="Location info"
          value={this.state.info}
          style={[styles.input, styles.input2]}
          placeholderTextColor="white"
        />
        <View style={styles.buttonContainer}>
          <TouchableOpacity onPress={this.addLocation}>
            <View style={styles.button}>
              <Text style={styles.buttonText}>Add Location</Text>
            </View>
          </TouchableOpacity>
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  locationsContainer: {
    paddingBottom: 104,
  },
  input: {
    height: 50,
    backgroundColor: colors.primary,
    color: 'white',
    paddingHorizontal: 8,
    position: 'absolute',
    width: '100%',
    bottom: 104,
    left: 0,
  },
  input2: {
    bottom: 52,
  },
  buttonContainer: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    width: '100%',
  },
  button: {
    height: 50,
    backgroundColor: colors.primary,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonText: {
    color: 'white',
  },
  locationContainer: {
    padding: 10,
    borderBottomColor: colors.primary,
    borderBottomWidth: 2,
  },
  locationName: {
    fontSize: 20,
  },
  locationInfo: {
    color: 'rgba(0, 0, 0, .5)',
  },
});

export default City;
