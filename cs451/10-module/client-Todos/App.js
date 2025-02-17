// ex01 - React Native Tutorial - Networking
import {useEffect, useState} from 'react';
import {ActivityIndicator, FlatList, Text, View, StyleSheet} from 'react-native';

const App = () => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getTodos = async () => {
    try {
      const response = await fetch('https://dummyjson.com/todos');
      const json = await response.json();
      setData(json.todos);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getTodos();
  }, []);

  return (
    <View style={{flex: 1, padding: 24}}>
      {isLoading ? (
        <ActivityIndicator />
      ) : (
        <FlatList
          data={data}
          keyExtractor={({id}) => id}
          renderItem={({item}) => (
            <View style={style.box}>
                <Text style={style.text}>ID: {item.id}</Text>
                <Text style={style.text}>Todo: {item.todo}</Text>
                <Text style={style.text}>
                    Completed: {item.completed ? '✔️' : '❌'}
                </Text>
            </View>
          )}
        />
      )}
    </View>
  );
};

const style = StyleSheet.create({
    container: {
        flex: 1,
        padding: 24,
    },
    box: {
        padding: 10,
        borderBottomColor: 'blue',
        borderBottomWidth: 1,
    },
    text: {
        fontSize: 18,
        fontWeight: 'bold',
        textAlign: 'left',
    },
});

export default App;