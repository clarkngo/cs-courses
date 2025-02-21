import React, { useEffect, useState } from 'react';
import { View, Text, TextInput, Button, FlatList, TouchableOpacity, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();

function TodoScreen() {
  const [todos, setTodos] = useState([]);
  const [newTodo, setNewTodo] = useState('');

  useEffect(() => {
    fetch('https://dummyjson.com/todos')
      .then((res) => res.json())
      .then((data) => setTodos(data.todos));
  }, []);

  const handleAddTodo = () => {
    if (newTodo.trim()) {
      const newItem = {
        id: todos.length + 1,
        todo: newTodo,
        completed: false,
      };
      setTodos([...todos, newItem]);
      setNewTodo('');
    }
  };

  const handleToggleDone = (id) => {
    setTodos(
      todos.map((item) =>
        item.id === id ? { ...item, completed: !item.completed } : item
      )
    );
  };

  const handleDeleteTodo = (id) => {
    setTodos(todos.filter((item) => item.id !== id));
  };

  return (
    <View style={styles.container}>
      <Text style={styles.header}>todos</Text>
      <TextInput
        placeholder="What needs to be done?"
        value={newTodo}
        onChangeText={setNewTodo}
        style={styles.input}
      />
      <Button title="Submit" onPress={handleAddTodo} />
      <FlatList
        data={todos}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.todoItem}>
            <Text style={item.completed ? styles.doneText : styles.todoText}>
              {item.todo}
            </Text>
            <TouchableOpacity
              style={styles.doneButton}
              onPress={() => handleToggleDone(item.id)}
            >
              <Text style={styles.doneButtonText}>Done</Text>
            </TouchableOpacity>
            <TouchableOpacity
              style={styles.deleteButton}
              onPress={() => handleDeleteTodo(item.id)}
            >
              <Text style={styles.deleteButtonText}>Delete</Text>
            </TouchableOpacity>
          </View>
        )}
      />
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Todos">
        <Stack.Screen name="Todos" component={TodoScreen} />
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
  header: {
    fontSize: 48,
    color: '#d9a7a7',
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ccc',
    marginBottom: 10,
    padding: 10,
    backgroundColor: '#fff',
  },
  todoItem: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
    backgroundColor: '#fff',
    padding: 10,
    borderRadius: 5,
  },
  todoText: {
    flex: 1,
    fontSize: 16,
  },
  doneText: {
    flex: 1,
    fontSize: 16,
    textDecorationLine: 'line-through',
    color: 'gray',
  },
  doneButton: {
    backgroundColor: 'green',
    padding: 5,
    marginRight: 5,
    borderRadius: 5,
  },
  doneButtonText: {
    color: 'white',
  },
  deleteButton: {
    backgroundColor: 'red',
    padding: 5,
    borderRadius: 5,
  },
  deleteButtonText: {
    color: 'white',
  },
});
