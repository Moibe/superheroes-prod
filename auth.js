//Conexión con Firebase
firebase.initializeApp(firebaseConfig);
const provider = new firebase.auth.GoogleAuthProvider();

firebase.auth().signInWithPopup(provider)
        .then((result) => {
            const user = result.user;
            updateUI(user);
            redirige(user);            
        }).catch((error) => {
            console.log(`Error al iniciar sesión: ${error.message}`);
        });