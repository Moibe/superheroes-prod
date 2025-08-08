import fireconfig1

js = f"""
function normal() {{
    console.log("Entré a aire.js")

    {fireconfig1.firebase_config}
    firebase.initializeApp(firebaseConfig);
    const provider = new firebase.auth.GoogleAuthProvider();
    firebase.auth().signOut();
    window.location.href = 'https://app.splashmix.ink/login';    
    }}

"""