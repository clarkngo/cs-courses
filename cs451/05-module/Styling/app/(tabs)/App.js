// Listing 5.1 Adding drop shadows to the ProfileCard

/*
    More depth with platform-specific styles; 
        drop shadows; 
        manipulating components with transformations such as translation, rotation, scaling, and skewing; 
            Transformations give you the power to manipulate components in two or three dimensions. 
            You can translate components from one position to another, rotate components, scale components to different sizes, and skew components. 

        and dynamically laying out components with flexbox.

    You’ll add a drop shadow to the entire ProfileCard container and to the circular image container.
    The reality is, on Android you’ll never get close to the shadow effects that can be produced on iOS with React Native out of the box. 
    If you really must have drop shadows on Android, then I suggest looking for a component on npm or yarn that does what you need.
*/
import React, { Component } from 'react';
/*
  Imports the Platform utility component to programmatically select styles based on the platform.
*/
import { Platform, Image, StyleSheet, Text, View} from 'react-native'; 

export default class App extends Component {
  render() {
    return (
      <View style={styles.container}>
        <View style={styles.cardContainer}>
          <View style={styles.cardImageContainer}>
            <Image style={styles.cardImage}
                   source={require('../../assets/images/user.png')}/>
          </View>
          <View>
            <Text style={styles.cardName}>
              John Doe
            </Text>
          </View>
          <View style={styles.cardOccupationContainer}>
            <Text style={styles.cardOccupation}> 
              React Native Developer
            </Text>
          </View>
          <View>
            <Text style={styles.cardDescription}>
              John is a really great JavaScript developer. He
              loves using JS to build React Native applications
              for iOS and Android.
            </Text>
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
      Adds a drop shadow to the card container based on the platform
    */
    cardContainer: {
        alignItems: 'center',
        borderColor: 'black',
        borderWidth: 3,
        borderStyle: 'solid',
        borderRadius: 20,
        backgroundColor: profileCardColor,
        width: 300,
        height: 400,
        ...Platform.select({ 
          ios: {
            shadowColor: 'black',
            shadowOffset: {
              height: 10
            },
            shadowOpacity: 1
          },
          android: {
            elevation: 15
          }
        })
    },
    /*
      Adds a drop shadow to the circular image container
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
        paddingTop: 15,
        ...Platform.select({ 
          ios: {
            shadowColor: 'black',
            shadowOffset: {
              height: 10,
            },
            shadowOpacity: 1
          },
          android: {
            borderWidth: 3,
            borderColor: 'black',
            elevation: 15
          }
        })
    },
    cardImage: {
        width: 80,
        height: 80
    },
    /*
        You can use the textShadowColor, textShadowOffset, and textShadowRadius properties to add a shadow to a Text element. 
        To create a shadow, you need to specify three things:
            The color
            The offset
            The radius

        The offset specifies the position of the shadow relative to the component casting the shadow. 
        The radius basically defines how blurry the shadow appears.
    */
    cardName: {
        color: 'white',
        fontWeight: 'bold',
        fontSize: 24,
        marginTop: 30,
        textShadowColor: 'black',
        textShadowOffset: {
            height: 5,
            width: 5
        },
        textShadowRadius: 3 
    },
    cardOccupationContainer: {
        borderColor: 'black',
        borderBottomWidth: 3
    },
    cardOccupation: {
        fontWeight: 'bold', 
        marginTop: 10,
        marginBottom: 10,
    },
    cardDescription: {
        fontStyle: 'italic', 
        marginTop: 10,
        marginRight: 40,
        marginLeft: 40,
        marginBottom: 10
    }
});