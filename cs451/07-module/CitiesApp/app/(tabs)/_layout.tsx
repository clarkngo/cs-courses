import { Slot } from 'expo-router';
import { CityProvider } from '../contexts/CityContext';

export default function RootLayout() {
  return (
    <CityProvider>
      <Slot />
    </CityProvider>
  );
}
