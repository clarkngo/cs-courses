// Listing 4.6 Application that toggles between light and dark themes
/*
    The application has a single button on the screen. 
    That button is enclosed by a small square box. 
    When the button is pressed, the themes will toggle. 
    When the light theme is selected, the button label will say White, the background will be white, and the box around the button will be black. 
    When the dark theme is selected, the button label will say Black, the background will be black, and the box around the button will be white. 
    
    Try changing the light theme to a different color. Notice how easy it is, because the colors are defined as constants in one place. 
    Try changing the button label in the dark theme to be the same color as the background instead of always white. 
*/
import React, { Component } from 'react';
import { Button, StyleSheet, View } from 'react-native';

/*
    Imports the getStyleSheet function from the externalized styles
*/
import getStyleSheet from './styles';

export default class App extends Component {
    /*
        Initializes the component’s state to show the light theme by default
        To avoid exceptions, the toggleTheme function must be bound to the component.
    */
    constructor(props) {
        super(props);
        this.state = {
            darkTheme: false
        };
        this.toggleTheme = this.toggleTheme.bind(this);
    }

    /*
        Toggles the theme value in state whenever the function is called
    */
    toggleTheme() {
        this.setState({darkTheme: !this.state.darkTheme})
    };

  render() {
    /*
        Uses the imported getStyleSheet function to get the appropriate stylesheet for whichever theme should be displayed.

        The React Native StyleSheet.flatten utility function converts the StyleSheet object into a JavaScript object, 
        which makes It much easier to get the backgroundColor.
    */
    const styles = getStyleSheet(this.state.darkTheme);
    const backgroundColor = StyleSheet.flatten(styles.container).backgroundColor;

    /*
        References the theme’s container style
        References the theme’s box style (the box border around the button)
        String representation of the color being used by the theme
        When the button is pressed, calls the toggleTheme function to alternate from one theme to another
    */
    return (
        <View style={styles.container}> 
            <View style={styles.box}>
                <Button title={backgroundColor} onPress={this.toggleTheme}/> 
            </View>
        </View>
    );
  }
}