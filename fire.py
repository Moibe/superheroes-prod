import fireconfig

js = f"""
function normal(a) {{

    console.log("Entré a fire.js @ BLOCKS y esto es a: ", a)
    resultado = localStorage.getItem('uid');
    console.log("1Éste es el usuario que obtuvo fuego cuando hay user auth desde afuera de fire: ", resultado);
    console.log("Estoy por hacer reload...");

    document.addEventListener('DOMContentLoaded', () => {{
    
    const reloadFlag = 'hasBeenReloaded';

    
    if (sessionStorage.getItem(reloadFlag) === null) {{
        

        console.log("Primera visita de la sesión. La página se recargará en 10 segundos.");

       
        sessionStorage.setItem(reloadFlag, 'true');

      
        setTimeout(() => {{
            window.location.reload();
        }}, 10000); // 10000 milisegundos = 10 segundos

    }} else {{
       
        console.log("La página ya se recargó en esta sesión. No se hará nada.");
    }}
    }});









    
      

    
    
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