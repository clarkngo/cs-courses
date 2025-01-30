// Listing 4.10 Incorporating border properties into the Profile Card
import React, { Component } from 'react';
import { Image, StyleSheet, View} from 'react-native';

/*
    https://icons8.com/icons/set/user
*/
export default class App extends Component  {
    render() {
        return (
            <View style={styles.container}>
                <View style={styles.cardContainer}>
                    <View style={styles.cardImageContainer}>
                        <Image style={styles.cardImage}        
                               source={require('../../assets/images/user.png')}/>
                    </View>
                </View>
            </View>
        );
    }
}

const profileCardColor = 'dodgerblue';

const styles = StyleSheet.create({
  container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center'
  },
  /*
      Aligns the circle in the horizontal center of the Profile Card.
  */
  cardContainer: {
      alignItems: 'center',
      borderColor: 'black',
      borderWidth: 3,
      borderStyle: 'solid',
      borderRadius: 20,
      backgroundColor: profileCardColor,
      width: 300,
      height: 400
  },
  /*
      Aligns the user image in the horizontal center of the circle.
      Provides space between the top of the circle and the top of the Profile Card.
      Provides padding between the inner part of the circle and the contained image
  */
  cardImageContainer: {
      alignItems: 'center',
      backgroundColor: 'white',
      borderWidth: 3,
      borderColor: 'black',
      width: 120,
      height: 120,
      borderRadius: 60,
      marginTop: 30,
      paddingTop: 15 
  },
  cardImage: {
      width: 80,
      height: 80
  }
});