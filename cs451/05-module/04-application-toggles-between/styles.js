// Listing 4.5 Dynamic stylesheets extracted from the main component file

import {StyleSheet} from 'react-native';

/*
    Constant defining the colors that will correspond to the light and dark themes.
*/
export const Colors = {
    dark: 'black',
    light: 'white'
};

/*
    JavaScript object to hold the base container styles.
*/
const baseContainerStyles = {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
};

/*
    JavaScript object to hold the base box styles.
*/
const baseBoxStyles = {
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    height: 150,
    width: 150
};

/*
    Spread Operator
    https://www.w3schools.com/react/react_es6_spread.asp
*/
/*
    Creates the stylesheet for the light theme.
*/
const lightStyleSheet = StyleSheet.create({
    container: {
        ...baseContainerStyles,
        backgroundColor: Colors.light
    },
    box: {
        ...baseBoxStyles,
        borderColor: Colors.dark
    }
});

/*
    Creates the stylesheet for the dark theme.
*/
const darkStyleSheet = StyleSheet.create({
    container: {
        ...baseContainerStyles,
        backgroundColor: Colors.dark
    },
    box: {
        ...baseBoxStyles,
        borderColor: Colors.light
    }
});

/*
    Function that will return the appropriate theme based on a Boolean value.
    Returns the dark theme if useDarkTheme is true; otherwise returns the light theme.
*/
export default function getStyleSheet(useDarkTheme) {
    return useDarkTheme ? darkStyleSheet : lightStyleSheet; 
}