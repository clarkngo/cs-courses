import React, { useState } from 'react';
import { View, Text, StyleSheet, TouchableWithoutFeedback, ScrollView } from 'react-native';
import { useLocalSearchParams } from 'expo-router';
import CenterMessage from '@/components/CenterMessage';

export default function Cities() {
  const [cities, setCities] = useState([]);

  return (
    <ScrollView contentContainerStyle={[!cities.length && { flex: 1 }]}>
      <View style={[!cities.length && { justifyContent: 'center', flex: 1 }]}>
        {!cities.length && <CenterMessage message="No saved cities!" />}
        {cities.map((item, index) => (
          <TouchableWithoutFeedback key={index}>
            <View style={styles.cityContainer}>
              <Text style={styles.city}>{item.city}</Text>
              <Text style={styles.country}>{item.country}</Text>
            </View>
          </TouchableWithoutFeedback>
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  cityContainer: {
    padding: 10,
    borderBottomWidth: 2,
    borderBottomColor: 'gray'
  },
  city: {
    fontSize: 20,
  },
  country: {
    color: 'rgba(0, 0, 0, .5)',
  }
});
