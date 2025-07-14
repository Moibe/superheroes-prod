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
            localStorage.setItem('usuario', user.uid);
            localStorage.setItem('usuario', user.email);
            localStorage.setItem('usuario', user.displayName); 
            localStorage.setItem('usuario', user.photoURL);   
        }} else {{
        console.log("No hay usuario...")        
            //Si el usuario se sale o no está. Importante: Revisar por que tengo comentado ésto.
            //localStorage.setItem('estadoUsuario', 'Desconectado');
            //localStorage.setItem('usuario', ""); 
        }}
    }})

    }}  

"""