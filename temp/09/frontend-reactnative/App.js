import React, { useState, useEffect } from 'react';
import { TextInput, FlatList, Button, Text, View, StyleSheet, ActivityIndicator, Pressable, Alert, ScrollView } from 'react-native';
import Collapsible from 'react-native-collapsible';
import { API_URL } from '@env';

const App = () => {
    const [searchTerm, setSearchTerm] = useState('');
    const [moviesData, setMoviesData] = useState([]);
    const [filteredData, setFilteredData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [loadingMore, setLoadingMore] = useState(false);
    const [selectedMovie, setSelectedMovie] = useState(null);
    const [similars, setSimilars] = useState({ actors: [], genres: [] });
    const [initialRecommendations, setInitialRecommendations] = useState([]);
    const [selectedMovies, setSelectedMovies] = useState([]);
    const [newRecommendations, setNewRecommendations] = useState([]);
    const [collapsed, setCollapsed] = useState(false);
    const toggleExpand = () => setCollapsed(!collapsed);
    const [messages, setMessages] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [userInput, setUserInput] = useState(''); // State for user input

    console.log("API_URL: " + API_URL);

    if (!API_URL) { 
        console.error("Error: API is not set or is empty.");
    }

    const handleChat = async () => {
        setIsLoading(true);
    
        try {
            const response = await fetch(`${API_URL}/chat`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    query_text: userInput,  // Sending user input as query_text
                }),
            });
    
            if (response.ok) {
                const reader = response.body.getReader();
                const decoder = new TextDecoder('utf-8');
    
                let accumulatedResponse = ''; // Accumulate the entire response
    
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;
    
                    // Decode the stream chunk
                    const decodedChunk = decoder.decode(value, { stream: true });
    
                    // Accumulate the response
                    accumulatedResponse += decodedChunk;
    
                    // Update the messages with the new chunk
                    setMessages((prevMessages) => [...prevMessages, decodedChunk]);
                }
            }
        } catch (error) {
            console.error('Error fetching chat:', error);
        }
        setIsLoading(false);
    };    

    const fetchMovies = async (pageNum) => {
        setLoading(true);
        try {
            const response = await fetch(`${API_URL}/movies?page=${pageNum}&limit=500`);
            const data = await response.json();
            const formattedData = data.map(movie => ({
                id: movie._id,
                title: movie.title,
                year: movie.year,
                genres: movie.genres || [], // Ensure genres is an array
                cast: movie.cast || [] // Ensure cast is an array
            }));
            setMoviesData(prevData => [...prevData, ...formattedData]);
            setFilteredData(prevData => [...prevData, ...formattedData]);
            setLoading(false);
            setLoadingMore(false);
        } catch (error) {
            console.error('Error fetching movies:', error);
            setLoading(false);
            setLoadingMore(false);
        }
    };

    const fetchSimilars = async (movie) => {
        try {
            const response = await fetch(`${API_URL}/similar`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    movie_id: movie.id,
                    genres: movie.genres || [], // Ensure genres is an array
                    cast: movie.cast || [], // Ensure cast is an array
                    title: movie.title || ""
                })
            });
            const data = await response.json();
            setSimilars(data);
        } catch (error) {
            console.error('Error fetching similar:', error);
        }
    };

    const fetchInitialRecommendations = async () => {
        try {
            const response = await fetch(`${API_URL}/initial-recommendations`);
            const data = await response.json();
            setInitialRecommendations(data);
        } catch (error) {
            console.error('Error fetching initial recommendations:', error);
        }
    };

    useEffect(() => {
        fetchMovies(1); // Load the first page of movies
        fetchInitialRecommendations(); // Fetch initial recommendations
    }, []);

    useEffect(() => {
        const filteredMovies = moviesData.filter(movie =>
            movie.title.toLowerCase().includes(searchTerm.toLowerCase())
        );
        setFilteredData(filteredMovies);
    }, [searchTerm, moviesData]);

    const handleSelectMovie = async (movie) => {
        setSelectedMovie(movie);
        fetchSimilars(movie);
    };

    const handleSelectInitialMovie = (movie) => {
        const isSelected = selectedMovies.some(selected => selected._id === movie._id);
        if (isSelected) {
            setSelectedMovies(prev => prev.filter(selected => selected._id !== movie._id));
        } else if (selectedMovies.length < 3) {
            setSelectedMovies(prev => [...prev, movie]);
        } else {
            Alert.alert('Limit Reached', 'You can only select up to 3 movies.');
        }
    };

    const submitSelectedMovies = async () => {
        try {
            const movieIds = selectedMovies.map(movie => movie._id);
            const response = await fetch(`${API_URL}/recommend`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ movieIds })
            });
            const data = await response.json();
            console.log(data);
            setNewRecommendations(data.recommendations);
            setCollapsed(true);
        } catch (error) {
            console.error('Error fetching new recommendations:', error);
        }
    };    

    const loadMoreMovies = () => {
        setLoadingMore(true);
        fetchMovies(Math.floor(moviesData.length / 10) + 1);
    };

    if (loading && !initialRecommendations.length) {
        return (
            <View style={styles.container}>
                <ActivityIndicator size="large" color="#0000ff" />
            </View>
        );
    }

    const getUniqueKey = (item, index) => item._id || item.id || index.toString();
    
    const renderMessage = ({ item }) => (
        <Text style={styles.messageText}>{item}</Text>
    );

    const clearMessages = () => {
        setMessages([]);
    };
    
    return (
        <View style={styles.container}>
            <Text style={styles.title}>Movie Recommender and Search Application</Text>
            <ScrollView contentContainerStyle={styles.scrollContainer}>

                {/* Chat  */}
                <View style={styles.searchContainer}>
                    <FlatList
                        data={messages}
                        renderItem={renderMessage}
                        keyExtractor={(item, index) => index.toString()} // Use index as key for simplicity
                        horizontal // Enable horizontal scrolling
                        style={styles.messageList}
                    />
                    <TextInput
                        style={styles.input}
                        placeholder="Type your message here..."
                        value={userInput}
                        onChangeText={text => setUserInput(text)}
                    />
                    <Button title="Send Message" onPress={handleChat} disabled={isLoading} />
                    <Button title="Clear Messages" onPress={clearMessages} color="red" />
                </View>

                {/* Collapsible Section */}
                <View style={styles.collapsibleContainer}>
                    <Pressable onPress={toggleExpand} style={styles.button}>
                        <Text style={styles.buttonText}>{collapsed ? 'Pick 3 Movies' : 'Hide'}</Text>
                    </Pressable>
                    <Collapsible collapsed={collapsed}>

                        {/* Initial Recommendations */}
                        <View style={styles.initialRecommendationsContainer}>
                            <Text style={styles.title}>Initial Recommendations - Pick 3 Movies</Text>
                            <FlatList
                                data={initialRecommendations}
                                keyExtractor={getUniqueKey}
                                renderItem={({ item }) => (
                                    <View style={styles.card}>
                                        <Text style={styles.itemTitle}>{item.genre}</Text>
                                        <FlatList
                                            data={item.movies}
                                            keyExtractor={getUniqueKey}
                                            renderItem={({ item }) => (
                                                <Pressable onPress={() => handleSelectInitialMovie(item)}>
                                                    <View style={[styles.card, selectedMovies.some(selected => selected._id === item._id) && styles.selectedCard]}>
                                                        <Text style={styles.itemTitle}>{item.title.length > 40 ? item.title.slice(0, 40) + '...' : item.title}</Text>
                                                        <Text style={[styles.itemText, { fontSize: 12 }]}>Genres: {item.genres?.join(', ') || 'N/A'}</Text>
                                                    </View>
                                                </Pressable>
                                            )}
                                            horizontal
                                        />
                                    </View>
                                )}
                                horizontal
                            />
                            <Pressable
                                style={[styles.button, { opacity: selectedMovies.length < 3 ? 0.5 : 1 }]}
                                onPress={submitSelectedMovies}
                                disabled={selectedMovies.length < 3}
                            >
                                <Text style={styles.buttonText}>Submit Selected Movies</Text>
                            </Pressable>
                        </View>

                    </Collapsible>
                </View>

                {/* Similar Movies */}
                {selectedMovie && (
                    <View style={styles.similarsContainer}>
                        <Text style={styles.title}>Similar Casts</Text>
                        <FlatList
                            horizontal
                            data={similars.actors}
                            keyExtractor={getUniqueKey}
                            renderItem={({ item }) => (
                                <View style={styles.card}>
                                    <Text style={styles.itemTitle}>{item.title}</Text>
                                    <Text style={styles.itemText}>Year: {item.year}</Text>
                                    <Text style={styles.itemText}>Genres: {item.genres?.join(', ') || 'N/A'}</Text>
                                    <Text style={styles.itemText}>Cast: {item.cast?.join(', ') || 'N/A'}</Text>
                                </View>
                            )}
                        />
                        <Text style={styles.title}>Similar Genres</Text>
                        <FlatList
                            horizontal
                            data={similars.genres}
                            keyExtractor={getUniqueKey}
                            renderItem={({ item }) => (
                                <View style={styles.card}>
                                    <Text style={styles.itemTitle}>{item.title}</Text>
                                    <Text style={styles.itemText}>Year: {item.year}</Text>
                                    <Text style={styles.itemText}>Genres: {item.genres?.join(', ') || 'N/A'}</Text>
                                    <Text style={styles.itemText}>Cast: {item.cast?.join(', ') || 'N/A'}</Text>
                                </View>
                            )}
                        />
                    </View>
                )}

                {/* New Recommendations */}
                {newRecommendations.length > 0 && (
                    <View style={styles.newRecommendationsContainer}>
                        <Text style={styles.title}>New Recommendations - Select any movie to get similar cast and genres</Text>
                        <FlatList
                            data={newRecommendations}
                            keyExtractor={getUniqueKey}
                            renderItem={({ item }) => (
                                <Pressable onPress={() => handleSelectMovie(item)}>
                                    <View style={styles.card}>
                                        <Text style={styles.itemTitle}>{item.title}</Text>
                                        <Text style={styles.itemText}>Year: {item.year}</Text>
                                        <Text style={styles.itemText}>Genres: {item.genres?.join(', ') || 'N/A'}</Text>
                                        <Text style={styles.itemText}>Cast: {item.cast?.join(', ') || 'N/A'}</Text>
                                    </View>
                                </Pressable>
                            )}
                        />
                    </View>
                )}

                {/* Movie Search */}
                <View style={styles.searchContainer}>
                    <Text style={styles.title}>Search for Movies - Select any movie to get similar cast and genres</Text>
                    <TextInput
                        style={styles.searchInput}
                        placeholder="Search movies..."
                        value={searchTerm}
                        onChangeText={setSearchTerm}
                    />
                    <Pressable onPress={loadMoreMovies} style={styles.button}>
                        <Text style={styles.buttonText}>Load More Movies</Text>
                    </Pressable>
                    <FlatList
                        data={filteredData}
                        keyExtractor={getUniqueKey}
                        renderItem={({ item }) => (
                            <Pressable onPress={() => handleSelectMovie(item)}>
                                <View style={styles.listItem}>
                                    <Text style={styles.itemTitle}>{item.title}</Text>
                                    <Text style={styles.itemText}>Year: {item.year}</Text>
                                    <Text style={styles.itemText}>Genres: {item.genres?.join(', ') || 'N/A'}</Text>
                                    <Text style={styles.itemText}>Cast: {item.cast?.join(', ') || 'N/A'}</Text>
                                </View>
                            </Pressable>
                        )}
                        ListFooterComponent={() => (
                            loadingMore ? <ActivityIndicator size="small" color="#0000ff" /> : 
                            <Pressable onPress={loadMoreMovies} style={styles.button}>
                                <Text style={styles.buttonText}>Load More Movies</Text>
                            </Pressable>
                        )}
                    />
                </View>
            </ScrollView>
        </View>
    );
};

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 10,
        backgroundColor: '#fff',
    },
    scrollContainer: {
        flexGrow: 1,
    },
    searchContainer: {
        marginTop: 5,
        borderWidth: 2,
        borderColor: '#000',
        borderRadius: 8,
        padding: 5,
        marginBottom: 5,
    },
    searchInput: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 10,
        paddingLeft: 8,
        borderRadius: 5,
    },
    listItem: {
        padding: 10,
        borderBottomWidth: 1,
        borderBottomColor: '#ccc',
    },
    itemTitle: {
        fontSize: 18,
        fontWeight: 'bold',
    },
    itemText: {
        fontSize: 14,
    },
    title: {
        fontSize: 20,
        fontWeight: 'bold',
    },
    initialRecommendationsContainer: {
        marginBottom: 10,
        borderWidth: 2,
        borderColor: '#000',
        borderRadius: 8,
        padding: 5,
    },
    newRecommendationsContainer: {
        marginTop: 10,
        marginBottom: 10,
        borderWidth: 2,
        borderColor: '#000',
        borderRadius: 8,
        padding: 5,
    },
    similarsContainer: {
        marginTop: 10,
        marginBottom: 10,
        borderWidth: 2,
        borderColor: '#000',
        borderRadius: 8,
        padding: 5,
    },
    card: {
        backgroundColor: '#f9f9f9',
        padding: 5,
        marginBottom: 10,
        borderRadius: 5,
    },
    selectedCard: {
        borderWidth: 2,
        borderColor: 'blue',
    },
    button: {
        backgroundColor: '#007bff',
        padding: 10,
        borderRadius: 5,
        alignItems: 'center',
    },
    buttonText: {
        color: '#fff',
        fontSize: 16,
    },
    messageList: {
        flex: 1,
        marginTop: 20,
    },
    messageText: {
        fontSize: 16,
        marginBottom: 10,
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        paddingHorizontal: 10,
        marginBottom: 10,
    },
});

export default App;
