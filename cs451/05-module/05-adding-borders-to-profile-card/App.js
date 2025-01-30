// Listing 4.7 Initial framework for the Profile Card component
/*
    The Profile Card is a rectangle with rounded corners and a circular section for a profile image.

    Display a 300 × 400 dodgerblue colored rectangle.

    Create a border around the profile container using borderWidth
    Round the corners of that border with borderRadius
    Create a border that looks like a circle by using a borderRadius half the size of the component’s width
    Position everything using margin and padding properties
*/
import React, { Component } from 'react';
import { StyleSheet, View} from 'react-native';

/*
    The outermost View element references the container style that centers the child View component.
    The inner View element will become the Profile Card component.
*/
export default class App extends Component {
    render() {
        return (
            <View style={styles.container}>
                <View style={styles.cardContainer}/>
            </View>
        );
    }
}

/*
    Defines the color for the Profile Card in a variable in case you need to use it in more than one place
*/
const profileCardColor = 'dodgerblue'; 

/*
    Style definition for the outermost container
    Style definition for the Profile Card container
    Sets the Profile Card backgroundColor to the constant set earlier
*/
const styles = StyleSheet.create({
    container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center'
    },
    cardContainer: {
      borderColor: 'black',
      borderWidth: 3,
      borderStyle: 'solid',
      borderRadius: 20,
      backgroundColor: profileCardColor,
      width: 300,
      height: 400
    },
    cardImageContainer: {
      backgroundColor: 'white',
      borderWidth: 3,
      borderColor: 'black',
      width: 120,
      height: 120,
      borderRadius: 60,
    },
    cardImage: {
      width: 80,
      height: 80
    }
  });