import React, { useState, useEffect } from 'react';
import { TextInput, FlatList, Text, View, StyleSheet, ActivityIndicator } from 'react-native';
import { API_URL } from '@env';

const App = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [moviesData, setMoviesData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);
    const [loading, setLoading] = useState(true);
    const fetchMovies = async () => {
        try {
          const response = await fetch(`${API_URL}/movies`);
          const data = await response.json();
          const formattedData = data.map(movie => ({
            title: movie.title,
            year: movie.year,
            genres: movie.genres,
            cast: movie.cast
          }));
          setMoviesData(formattedData);
          setFilteredData(formattedData);
          setLoading(false);
        } catch (error) {
          console.error('Error fetching movies:', error);
          setLoading(false);
        }
    };
      
    useEffect(() => {
      fetchMovies();
    }, []);
    
    useEffect(() => {
        const filteredMovies = moviesData.filter(movie =>
          movie.title.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setFilteredData(filteredMovies);
    }, [searchTerm, moviesData]);

    if (loading) {
    return (
        <View style={styles.container}>
        <ActivityIndicator size="large" color="#0000ff" />
        </View>
    );
    }
    
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
                        <Text style={styles.itemText}>Year: {item.year}</Text>
                        <Text style={styles.itemText}>Genres: {item.genres.join(', ')}</Text>
                        <Text style={styles.itemText}>Cast: {item.cast.join(', ')}</Text>
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
