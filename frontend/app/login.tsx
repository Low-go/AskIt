import { SignInForm } from "@/components/sign-in-form";
import { ScrollView, View, Alert } from "react-native"
import { useState } from "react";
import { useSession } from "@/authContext";
import { router } from "expo-router";

export default function LoginScreen(){

  const {signIn} = useSession();
  const [isLoading, setIsLoading] = useState(false);
  // note to self not sure if i need a use router here, i think only in the child coomponent

  const handleSignIn = async(email:string, password: string)=>{
    setIsLoading(true);
    const success = await signIn(email, password);

    setIsLoading(false);

    if (success){
      router.replace('/(tabs)')
    } else {
      Alert.alert('Login Failed', 'Invalid email or password');
    }
  }
    return (
    <ScrollView
      keyboardShouldPersistTaps="handled"
      contentContainerClassName="sm:flex-1 items-center justify-center p-4 py-8 sm:py-4 sm:p-6"
      keyboardDismissMode="interactive"
    >
      <View className="w-full max-w-sm">
        <SignInForm 
          onSignIn={handleSignIn}
          isLoading={isLoading}
        />
      </View>
    </ScrollView>
  );
    
}