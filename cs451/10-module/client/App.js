import React, { useEffect, useState } from 'react';
import { View, Text, TextInput, Button, FlatList, TouchableOpacity, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

const API_URL = 'https://super-telegram-77q6jrvv54ghwqjq-5050.app.github.dev/record';

function RecordScreen() {
  const [records, setRecords] = useState([]);
  const [name, setName] = useState('');
  const [position, setPosition] = useState('');
  const [level, setLevel] = useState('');
  const [editingRecord, setEditingRecord] = useState(null);

  useEffect(() => {
    fetchRecords();
  }, []);

  const fetchRecords = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setRecords(data);
    } catch (error) {
      console.error('Error fetching records:', error);
    }
  };

  const addRecord = async () => {
    if (!name || !position || !level) return;

    const newRecord = { name, position, level };
    await fetch(API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newRecord),
    });

    fetchRecords();
    setName('');
    setPosition('');
    setLevel('');
  };

  const deleteRecord = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' });
    fetchRecords();
  };

  const updateRecord = async () => {
    if (!editingRecord) return;

    await fetch(`${API_URL}/${editingRecord._id}`, {
      method: 'PATCH',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, position, level }),
    });

    fetchRecords();
    setEditingRecord(null);
    setName('');
    setPosition('');
    setLevel('');
  };

  const startEditing = (record) => {
    setEditingRecord(record);
    setName(record.name);
    setPosition(record.position);
    setLevel(record.level);
  };

  return (
    <View style={styles.container}>
      <TextInput style={styles.input} placeholder="Name" value={name} onChangeText={setName} />
      <TextInput style={styles.input} placeholder="Position" value={position} onChangeText={setPosition} />
      <TextInput style={styles.input} placeholder="Level" value={level} onChangeText={setLevel} />
      {editingRecord ? (
        <Button title="Update Record" onPress={updateRecord} />
      ) : (
        <Button title="Add Record" onPress={addRecord} />
      )}
      
      <FlatList
        data={records}
        keyExtractor={(item) => item._id.toString()}
        renderItem={({ item }) => (
          <View style={styles.recordItem}>
            <Text style={styles.recordText}>{item.name}</Text>
            <Text style={styles.recordText}>{item.position}</Text>
            <Text style={styles.recordText}>{item.level}</Text>
            <View style={styles.buttonContainer}>
              <TouchableOpacity style={styles.editButton} onPress={() => startEditing(item)}>
                <Text style={styles.buttonText}>Edit</Text>
              </TouchableOpacity>
              <TouchableOpacity style={styles.deleteButton} onPress={() => deleteRecord(item._id)}>
                <Text style={styles.buttonText}>Delete</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      />
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Records">
        <Stack.Screen name="Records" component={RecordScreen} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: '#f7f7f7',
    flex: 1,
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 10,
    padding: 10,
    backgroundColor: '#fff',
    borderRadius: 5,
  },
  recordItem: {
    backgroundColor: '#fff',
    padding: 15,
    borderRadius: 8,
    marginBottom: 10,
    elevation: 2,
  },
  recordText: {
    fontSize: 16,
    fontWeight: 'bold',
    marginBottom: 5,
  },
  buttonContainer: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 10,
  },
  editButton: {
    backgroundColor: '#4CAF50',
    padding: 8,
    borderRadius: 5,
  },
  deleteButton: {
    backgroundColor: '#FF5733',
    padding: 8,
    borderRadius: 5,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
});
