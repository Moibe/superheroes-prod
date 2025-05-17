import fireconfig

js = f"""
function normal() {{
    console.log("Entré a aire.js")
    console.log("a")

    {fireconfig.firebase_config}
    firebase.initializeApp(firebaseConfig);
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signOut()
    
    }}

"""