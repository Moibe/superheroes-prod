import fireconfig

js = f"""
function normal(a) {{

    console.log("Entré a fire.js @ BLOCKS y esto es a: ", a)
    resultado = localStorage.getItem('uid');
    console.log("1Éste es el usuario que obtuvo fuego cuando hay user auth desde afuera de fire: ", resultado);
    const urlParams = new URLSearchParams(window.location.search);
    console.log("Estos son los URL params")
    console.log(urlParams)
    console.log("Estoy por hacer reload...");
    if (urlParams.get('reload') === 'true') {{
        console.log("Parámetro 'reload=true' encontrado. Recargando la página en 10 segundos...");
        // Elimina el parámetro 'reload' de la URL antes de la recarga
        urlParams.delete('reload');
        const newUrl = `${{window.location.pathname}}?${{urlParams.toString()}}${{window.location.hash}}`;
        history.pushState(null, '', newUrl);
        
        // Ejecuta la recarga de la página con un retraso de 10 segundos
        setTimeout(() => {{
            window.location.reload();
        }}, 10000); // 10000 milisegundos = 10 segundos
    }}

    document.addEventListener('DOMContentLoaded', () => {{
    
    console.log("Document DOC content loaded...");
    const reloadFlag = 'hasBeenReloaded';
    
    if (localStorage.getItem(reloadFlag) === null) {{
        

        console.log("Primera visita de la sesión. La página se recargará en 10 segundos.");

       
        localStorage.setItem(reloadFlag, 'true');

      
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