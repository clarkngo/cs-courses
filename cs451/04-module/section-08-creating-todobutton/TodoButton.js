// Listing 3.18 Creating TodoButton.js
import React from 'react'
import { Text, TouchableHighlight, StyleSheet } from 'react-native'

/*
    Create a button component called TodoButton to pass in to the todo
      Takes onPress, complete, and name as props.
    Checks whether complete is true, and applies a style called "complete."
    Checks whether the name property equals “Delete” and, if so, applies a style called "delateButton."
*/
const TodoButton = ({ onPress, complete, name }) => (  
  <TouchableHighlight
    onPress={onPress}
    underlayColor='#efefef'
    style={styles.button}>
    <Text style={[
      styles.text,
      complete ? styles.complete : null,  
      name === 'Delete' ? styles.deleteButton : null ]} 
     >
      {name}
    </Text>
  </TouchableHighlight>
)

const styles = StyleSheet.create({
  button: {
    alignSelf: 'flex-end',
    padding: 7,
    borderColor: '#ededed',
    borderWidth: 1,
    borderRadius: 4,
    marginRight: 5
  },
  text: {
    color: '#666666'
  },
  complete: {
    color: 'green',
    fontWeight: 'bold'
  },
  deleteButton: {
    color: 'rgba(175, 47, 47, 1)'
  }
})

export default TodoButton