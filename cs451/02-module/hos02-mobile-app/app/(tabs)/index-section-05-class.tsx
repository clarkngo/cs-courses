import { View, Text } from 'react-native';
import { Component } from 'react';

class HomeScreen extends Component {
  render() {
    return (
      <View
        style={
          {
            flex: 1,
            justifyContent: 'center',
            alignItems: 'center',
            backgroundColor: 'white'
          }
        }
      >
        <Text>Hello, world! Class Component!</Text>
      </View>
    );
  }
}

export default HomeScreen;
