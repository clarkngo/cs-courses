import React from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';
import uuid from 'react-native-uuid';
import { colors } from '../theme';

class AddCity extends React.Component {
  state = {
    city: '',
    country: '',
  };

  onChangeText = (key, value) => {
    this.setState({ [key]: value });
  };

  submit = () => {
    const { city, country } = this.state;
    if (city === '' || country === '') {
      alert('please complete form');
      return;
    }
    const newCity = {
      city,
      country,
      id: uuid.v4(),
      locations: [],
    };
    this.props.addCity(newCity); // ✅ State lifted up, no params anymore
    this.setState(
      {
        city: '',
        country: '',
      },
      () => {
        this.props.navigation.navigate('Cities');
      }
    );
  };

  render() {
    return (
      <View style={styles.container}>
        <Text style={styles.heading}>Cities</Text>
        <TextInput
          placeholder="City name"
          onChangeText={(val) => this.onChangeText('city', val)}
          style={styles.input}
          value={this.state.city}
        />
        <TextInput
          placeholder="Country name"
          onChangeText={(val) => this.onChangeText('country', val)}
          style={styles.input}
          value={this.state.country}
        />
        <TouchableOpacity onPress={this.submit}>
          <View style={styles.button}>
            <Text style={styles.buttonText}>Add City</Text>
          </View>
        </TouchableOpacity>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  button: {
    height: 50,
    backgroundColor: '#666',
    justifyContent: 'center',
    alignItems: 'center',
    margin: 10,
  },
  buttonText: {
    color: 'white',
    fontSize: 18,
  },
  heading: {
    color: 'white',
    fontSize: 40,
    marginBottom: 10,
    alignSelf: 'center',
  },
  container: {
    backgroundColor: colors.primary,
    flex: 1,
    justifyContent: 'center',
  },
  input: {
    margin: 10,
    backgroundColor: 'white',
    paddingHorizontal: 8,
    height: 50,
  },
});

export default AddCity;
