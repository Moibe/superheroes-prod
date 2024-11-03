import sulkuPypi
import gradio as gr

def display_tokens(request: gr.Request):

    #Para desplegar o no desplegar, necesitamos saber si el usuario es new user.
    flag = sulkuPypi.getFlag(sulkuPypi.encripta(request.username).decode("utf-8"))
    print("La flag obtenida es: ", flag)
    #FUTURE quizá das doble vuelta decodificando porque haya lo vuelves a encodear, prueba enviando sin decode...
    #...llegaría codificado a encripta y prueba allá no encode.
    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"))
    display = actualizar_creditos(tokens, request.username)
    
    return display

def actualizar_creditos(nuevos_creditos, usuario):

     html_credits = f"""
     <div>
     <div style="text-align: left;">👤<b>Username: </b> {usuario}</div><div style="text-align: right;">💶<b>Credits Available: </b> {nuevos_creditos}</div>
     </div>
                       """
     
     return html_credits