import fireconfig

js = f"""
function normal(a) {{

    console.log("Entré a fire.js @ BLOCKS")
    {fireconfig.firebase_config}
    firebase.initializeApp(firebaseConfig);
    const provider = new firebase.auth.GoogleAuthProvider();
    
    firebase.auth().onAuthStateChanged((user) => {{
        if (user) {{
        console.log("Hay usuario...", user)
            localStorage.setItem('estadoUsuario', 'Conectado');
            localStorage.setItem('uid', user.uid);
            localStorage.setItem('email', user.email);
            localStorage.setItem('name', user.displayName); 
            localStorage.setItem('photo', user.photoURL);   
        }} else {{
        console.log("No hay usuario...")        
            //Si el usuario se sale o no está. Importante: Revisar por que tengo comentado ésto.
            //localStorage.setItem('estadoUsuario', 'Desconectado');
            //localStorage.setItem('usuario', ""); 
        }}
    }})

    }}  

"""