#Si está en uso, es con el que lee auth de la correspondiente base.
import globales 

if globales.firebase_auth == 'dev':
  
  firebase_config = """
  const firebaseConfig = {
  apiKey: "AIzaSyDGYZJ87hn-RfveqC_BydFQEJTMSvS7eK4",
  authDomain: "splashmix-88e15.firebaseapp.com",
  projectId: "splashmix-88e15",
  storageBucket: "splashmix-88e15.firebasestorage.app",
  messagingSenderId: "429463695136",
  appId: "1:429463695136:web:5843b892e8761560f77145",
  measurementId: "G-PHPJCWFF9L"
};
    """
else:
  firebase_config = """
  const firebaseConfig = {
  apiKey: "AIzaSyBSlzBn-wxB4PrldzfAF8_xtEW2E6HIqJ8",
  authDomain: "splashmix-ai.firebaseapp.com",
  projectId: "splashmix-ai",
  storageBucket: "splashmix-ai.firebasestorage.app",
  messagingSenderId: "1093510950901",
  appId: "1:1093510950901:web:7f2e18ad5f959af42d7abc",
  measurementId: "G-V2L2EG9LPZ"
};
    """