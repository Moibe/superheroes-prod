js = f"""
function funcion() {{
    console.log("Ésto es un console log normal desde fuego.js @ PRECARGA") 
        
    resultado = localStorage.getItem('usuario');
    console.log("Éste es el usuario que obtuvo fuego: ", resultado)
    // Verificar si resultado está vacío
    if (!resultado || resultado === "" || resultado === "null" || resultado === "undefined") {{
    console.log("Resultado está vacío o es null/undefined, redireccionando...");
    }} else {{
    console.log("Resultado no está vacío, no se redirecciona.");
    }}
    return resultado       
    }}

"""
