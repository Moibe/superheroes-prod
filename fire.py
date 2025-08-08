import fireconfig

js = f"""
function normal(a) {{

    console.log("Entré a fire.js @ BLOCKS y esto es a: ", a)
    resultado = localStorage.getItem('uid');
    console.log("1Éste es el usuario que obtuvo fuego cuando hay user auth desde afuera de fire: ", resultado);
    console.log("Estoy por hacer reload...");
    recargado = localStorage.getItem('reloaded');
    console.log("Reloaded en localstorage es:", recargado);
    if (recargado === 'false') {{
      console.log("Recargando por que estaba en false...");
      setTimeout(() => {{
  window.location.reload();
    }}, 10000);
    }}    
    
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
            resultado = localStorage.getItem('uid');
            console.log("Éste es el usuario que obtuvo fuego cuando hay user auth: ", resultado)   
        }} else {{
        console.log("No hay usuario...") 
        resultado = localStorage.getItem('uid');
        console.log("Éste es el usuario que obtuvo fuego cuando no hay usuario auth: ", resultado)       
            //Si el usuario se sale o no está. Importante: Revisar por que tengo comentado ésto.
            //localStorage.setItem('estadoUsuario', 'Desconectado');
            //localStorage.setItem('usuario', ""); 
        }}
    }})

    console.log("Estoy por retornar resultado...")
    return resultado

    }}  

"""