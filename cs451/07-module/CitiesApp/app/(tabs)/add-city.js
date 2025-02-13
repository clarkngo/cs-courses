import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';
import uuid from 'react-native-uuid';
import { colors } from '../components/theme';
import { useRouter } from 'expo-router';
import { useCity } from '../contexts/CityContext';

export default function AddCity() {
  const { addCity } = useCity();
  const [city, setCity] = useState('');
  const [country, setCountry] = useState('');
  const router = useRouter();

  const submit = () => {
    if (!city || !country) {
      alert('Please complete the form');
      return;
    }

    const newCity = {
      city,
      country,
      id: uuid.v4(),
      locations: [],
    };

    addCity(newCity);

    setCity('');
    setCountry('');
    router.setParams({ screen: 'cities' });
  };

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Add City</Text>
      <TextInput
        placeholder="City name"
        onChangeText={setCity}
        style={styles.input}
        value={city}
      />
      <TextInput
        placeholder="Country name"
        onChangeText={setCountry}
        style={styles.input}
        value={country}
      />
      <TouchableOpacity onPress={submit}>
        <View style={styles.button}>
          <Text style={styles.buttonText}>Add City</Text>
        </View>
      </TouchableOpacity>
    </View>
  );
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
