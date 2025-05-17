import fireconfig

js = f"""
function normal() {{
    console.log("Entré a aire.js")
    console.log("a")

    {fireconfig.firebase_config}
    firebase.initializeApp(firebaseConfig);
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signOut()
    console.log("Deslogueado 3...)
    console.log("Deslogueado 2...)
    console.log("Deslogueado 1...)
    window.location.href = 'https://app.splashmix.ink/login';    
    }}

"""