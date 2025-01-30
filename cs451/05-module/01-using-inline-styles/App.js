// Listing 4.1 Using inline styles
import React, { Component } from 'react'
import { Text, View } from 'react-native'

/*
  Inline style
  Applies an inline style to a React Native component.
  Applies multiple inline styles at once.
*/
export default class App extends Component {
  render () {
    return (
      <View style={{marginLeft: 20, marginTop: 20}}>
        <Text style={{fontSize: 18, color: 'red'}}>Listing 4.1 Some Text</Text>
      </View>
    )
  }
}