// Listing 4.3 Externalizing a component’s stylesheets
/*
    External style
    Having styles specified in one place rather than inline on many components makes it easier to apply changes across the entire application.
*/
import { StyleSheet } from 'react-native'

/*
    Creates a stylesheet, and saves it in the styles constant.
    Defines a style for the container. It can be referenced by the component as styles.container.
    Defines a style for the countContainer. It can be referenced by the component as styles.countContainer.
    Defines a style for the countText. It can be referenced by the component as styles.countText.
    
    Creates a second stylesheet, and saves it in the buttons constant
    Defines a style for the primary button. It can be referenced by the component as buttons.primary.
    
    Exports both the styles and buttons stylesheets so the component will have access to the constants
*/
const styles = StyleSheet.create({
  container: { 
    flex: 1,
    marginTop: 150,
  },
  countContainer: {
    alignItems: 'center',
    padding: 10,
  },
  countText: {
    fontSize: 18, 
    color: 'red'
 }
})

const buttons = StyleSheet.create({
  primary: {
    height: 70,
    backgroundColor: 'red',
    justifyContent: 'center',
    alignItems: 'center',
    marginLeft: 20,
    marginRight: 20
  },
  buttonText: {
    color: 'white',
  }
})

export { styles, buttons }