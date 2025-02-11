import React, { useState } from 'react';
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';
import uuid from 'react-native-uuid';
import { useRouter } from 'expo-router';

export default function AddCity() {
  const [city, setCity] = useState('');
  const [country, setCountry] = useState('');
  const router = useRouter();

  const submit = () => {
    if (city === '' || country === '') {
      alert('Please complete the form');
      return;
    }

    // Normally, you'd save this to state or context, for now just navigating back
    console.log('Added City:', { city, country, id: uuid() });

    setCity('');
    setCountry('');
    router.push('/cities'); // Navigate back to Cities screen
  };

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Add a City</Text>
      <TextInput
        placeholder='City name'
        onChangeText={setCity}
        style={styles.input}
        value={city}
      />
      <TextInput
        placeholder='Country name'
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
  container: {
    flex: 1,
    justifyContent: 'center',
    padding: 20
  },
  heading: {
    fontSize: 24,
    fontWeight: 'bold',
    textAlign: 'center',
    marginBottom: 20
  },
  input: {
    marginBottom: 15,
    borderWidth: 1,
    padding: 10
  },
  button: {
    backgroundColor: 'blue',
    padding: 10,
    alignItems: 'center'
  },
  buttonText: {
    color: 'white',
    fontWeight: 'bold'
  }
});
