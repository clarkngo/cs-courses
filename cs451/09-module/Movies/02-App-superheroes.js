// ex01 - React Native Tutorial - Networking
import {useEffect, useState} from 'react';
import {ActivityIndicator, FlatList, Text, View, StyleSheet} from 'react-native';

const App = () => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState([]);

  const getSuperHeroes = async () => {
    try {
      const response = await fetch('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json');
      const json = await response.json();
      setData(json.members);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    getSuperHeroes();
  }, []);

  return (
    <View style={style.container}>
        {isLoading ? (
            <ActivityIndicator />
        ) : (
            <FlatList
            data={data}
            keyExtractor={({ id }) => id}
            renderItem={({ item }) => (
                <View style={style.box}>
                <Text style={style.text}>
                    Name: {item.name}
                </Text>
                <Text style={style.text}>
                    Age: {item.age}
                </Text>
                <Text style={style.text}>
                    Secret Identity: {item.secretIdentity}
                </Text>
                <Text style={style.text}>
                    The First Power: {item.powers[0]}
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