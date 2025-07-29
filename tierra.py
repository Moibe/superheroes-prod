js = f"""
function funcion() {{
    console.log("Ésto es un console log normal desde magma.js @ PRECARGA")  
    localStorage.setItem('estadoUsuario', 'Desconectado');
    localStorage.removeItem('uid');
    localStorage.removeItem('email');
    localStorage.removeItem('name'); 
    localStorage.removeItem('photo');         
    
    window.location.href = 'https://app.splashmix.ink/login'
    
    }}

"""