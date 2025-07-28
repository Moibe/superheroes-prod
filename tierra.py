js = f"""
function funcion(a) {{
    console.log("Ésto es un console log desde tierra.js @ comprar.click") 
    console.log("Trajo a a?: ", a)       
    resultado = localStorage.getItem('uid');
    console.log("Éste es el usuario que obtuvo tierra: ", resultado)
    // Verificar si resultado está vacío
    if (!resultado || resultado === "" || resultado === "null" || resultado === "undefined") {{
    console.log("Resultado está vacío o es null/undefined, redireccionando...");
    }} else {{
    console.log("Resultado no está vacío, no se redirecciona.");
    }}
    return resultado       
    }}

"""