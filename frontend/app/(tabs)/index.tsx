import { Text, View, StyleSheet } from 'react-native';
import { useContext } from 'react';
import { useSession } from '../../authContext';


export default function HomeScreen() {
  const { signOut } = useSession();
  
  return (
    <View style={styles.container}>
      <Text style={styles.helloText}>Hello World</Text>
      <Text style={styles.signOutText} onPress={signOut}>
        Sign Out
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  helloText: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  signOutText: {
    fontSize: 18,
    color: '#007AFF',
    marginTop: 20,
  },
});