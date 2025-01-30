// Listing 4.4 Importing external stylesheets
import React, {Component} from 'react'
import {Text, TouchableHighlight, View} from 'react-native'

/*
    Imports multiple stylesheets exported from styles.js
*/
import { styles, buttons } from './styles'

class App extends Component {
  state = {
    count: 0,
  };

  onPress = () => {
    this.setState({
      count: this.state.count + 1,
    });
  };

  /*
    Reference to the styles.container, styles.countContainer, and styles.countText styles created in styles.js
    Reference to the buttons.primary style created in styles.js
  */
  render() {
    return (
      <View style={styles.container}>
        <TouchableHighlight onPress={this.onPress}>
          <View style={buttons.primary}>
            <Text style={buttons.buttonText}>Listing 4.4 Touch Here</Text>
          </View>
        </TouchableHighlight>
        <View style={styles.countContainer}>
          <Text style={styles.countText}>
            {this.state.count ? this.state.count : null}
          </Text>
        </View>
      </View>
    )
  }
}

export default App