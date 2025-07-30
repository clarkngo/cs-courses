import React, { useState, useEffect } from 'react';
import { TextInput, FlatList, Text, View, StyleSheet } from 'react-native';

// Sample data for movies
const moviesData = [
  { title: 'Inception', genre: 'Sci-Fi', year: 2010 },
  { title: 'The Dark Knight', genre: 'Action', year: 2008 },
  { title: 'Interstellar', genre: 'Sci-Fi', year: 2014 },
  { title: 'The Prestige', genre: 'Thriller', year: 2006 },
  { title: 'Memento', genre: 'Mystery', year: 2000 }
];

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [filteredData, setFilteredData] = useState(moviesData);

  useEffect(() => {
    const filteredMovies = moviesData.filter(movie =>
      movie.title.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setFilteredData(filteredMovies);
  }, [searchTerm]);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Movie List</Text>
      <TextInput
        style={styles.searchInput}
        placeholder="Search movies..."
        value={searchTerm}
        onChangeText={setSearchTerm}
      />
      <FlatList
        data={filteredData}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <View style={styles.listItem}>
            <Text style={styles.itemTitle}>{item.title}</Text>
            <Text style={styles.itemText}>Genre: {item.genre}</Text>
            <Text style={styles.itemText}>Year: {item.year}</Text>
          </View>
        )}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  searchInput: {
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 20,
    paddingHorizontal: 10,
  },
  listItem: {
    borderBottomWidth: 1,
    borderBottomColor: '#ccc',
    paddingVertical: 10,
  },
  itemTitle: {
    fontSize: 18,
    fontWeight: 'bold',
  },
  itemText: {
    fontSize: 14,
  },
});

export default App;
