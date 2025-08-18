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
        // 1. Elimina el parámetro 'reload'
        urlParams.delete('reload');
        
        // 2. Construye la URL sin el parámetro
        let newUrl;
        if (urlParams.toString()) {{
            // Si hay otros parámetros, los mantiene
            newUrl = `${{window.location.pathname}}?${{urlParams.toString()}}${{window.location.hash}}`;
        }} else {{
            // Si no quedan parámetros, quita el signo de interrogación
            newUrl = `${{window.location.pathname}}${{window.location.hash}}`;
        }}
        
        // 3. Modifica la URL en la barra de direcciones
        history.pushState(null, '', newUrl);
        
        // Ejecuta la recarga de la página con un retraso de 10 segundos
        setTimeout(() => {{
            window.location.reload();
        }}, 500); //medio segundo
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