import firebase

js = f"""
function normal(a) {{

    console.log("Entré a fire.js")
    {firebase.firebase_config}
    firebase.initializeApp(firebaseConfig);
    const provider = new firebase.auth.GoogleAuthProvider();
    
    firebase.auth().onAuthStateChanged((user) => {{
        if (user) {{
            localStorage.setItem('estadoUsuario', 'Conectado');
            localStorage.setItem('usuario', user.uid);    
        }} else {{
            //Si el usuario se sale o no está.
            localStorage.setItem('estadoUsuario', 'Desconectado');
            localStorage.setItem('usuario', ""); 
        }}
    }})

    //Esto es para en dado caso usar rememberedAccounts (que no siempre, y no se bajo que circunstancias, aparece.)
    //const rememberedAccounts = localStorage.getItem('firebaseui::rememberedAccounts');
    //console.log(rememberedAccounts)      
    }}

"""