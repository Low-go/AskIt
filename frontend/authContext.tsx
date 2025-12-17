import { use, createContext, type PropsWithChildren} from 'react';
import { useStorageState } from './useStorageState';

const AuthContext = createContext<{
    signIn: (email: string, password: string) => Promise<boolean>;
    signOut: ()=> void;
    session?: string | null;
    isLoading: boolean
}>({
    signIn: async()=> false,
    signOut: ()=> null,
    session: null,
    isLoading: false
});

//hook used to access the user info
export function useSession(){
    const value = use(AuthContext);
    if (!value){
        throw new Error('useSession must be wrapped in a <SessionProvider/>');
    }

    return value;
}

// Mock credentials/ Delete later
const MOCK_USER = {
    email: "test@gmail.com",
    password: "test123"
};

// Mock JWT token (looks real but isn't)
const MOCK_JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZW1haWwiOiJ0ZXN0QGV4YW1wbGUuY29tIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c";


export function SessionProvider({children}: PropsWithChildren){
    const[[isLoading, session],setSession] = useStorageState('session');

    return (
        <AuthContext.Provider
            value={{
                signIn: async(email: string, password: string) => {
                    //TODO,Note perform sign in logic here, Come back to this
                    await new Promise(resolve => setTimeout(resolve, 1000))
                    
                    // Check mock credentials
                    if (email === MOCK_USER.email && password === MOCK_USER.password) {
                        // Store mock JWT token
                        setSession(MOCK_JWT_TOKEN);
                        return true;
                    }
                    
                    // Login failed
                    return false;
                },
                signOut: () => {
                    setSession(null);
                },
                session,
                isLoading,
            }}>
                {children}
            </AuthContext.Provider>
    );
}