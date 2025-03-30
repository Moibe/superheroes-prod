import firebase

js = f"""
function normal(a) {{

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

# js = f"""

# function normal(a) {{
#     {firebase.firebase_config}
#     firebase.initializeApp(firebaseConfig);
#     const provider = new firebase.auth.GoogleAuthProvider();

#     const user = firebase.auth.currentUser;

#     if (user) {{
#     //El usuario ha iniciado sesión
#     const uid = user.uid;
#     console.log('Usuario actual:', uid);
#     // Aquí puedes realizar acciones basadas en el estado de autenticación en ese momento
    
#     }} else {{
#     // El usuario ha cerrado sesión
#     console.log('No hay usuario actual');
#     // Aquí puedes realizar acciones si no hay un usuario autenticado
#     }}

#     }}

# """