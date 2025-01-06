import React, { Component } from 'react'
import { Text, View, ScrollView, StyleSheet } from 'react-native'
import Heading from './Heading';

class App extends Component {
  constructor() {
    super();
    this.state = {
        inputValue: '',
        todos: [],
        type: 'All',
    };
  }
  render() {
    return (
      <View style={styles.container}>
        <ScrollView keyboardShouldPersistTaps="always" style={styles.content}>
          <Heading />
        </ScrollView>
      </View>
    )
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5'
  },
  content: {
    flex: 1,
    paddingTop: 60
  }
})

export default App