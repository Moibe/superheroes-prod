import fireconfig

js = f"""
function normal(a) {{

    console.log("Entré a fire.js")
    console.log(window.location.search)
    {fireconfig.firebase_config}
    firebase.initializeApp(firebaseConfig);
    const provider = new firebase.auth.GoogleAuthProvider();
    
    firebase.auth().onAuthStateChanged((user) => {{
        if (user) {{
        console.log("Hay usuario...", user)
            localStorage.setItem('estadoUsuario', 'Conectado');
            localStorage.setItem('usuario', user.uid);    
        }} else {{
        console.log("No hay usuario...")
            //Si el usuario se sale o no está.
            localStorage.setItem('estadoUsuario', 'Desconectado');
            localStorage.setItem('usuario', ""); 
            //window.location.href = 'https://app.splashmix.ink/login';
        }}
    }})
      
    }}

"""