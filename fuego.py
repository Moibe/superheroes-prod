import firebase

js = f"""
function funcion() {{
    console.log("Ésto es un console log normal desde fuego...") 
    resultado = localStorage.getItem('usuario');
    console.log("Éste es el usuario que obtuvo fuego: ", resultado)
    return resultado       
    }}

"""
