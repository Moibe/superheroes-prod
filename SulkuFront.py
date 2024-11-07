import sulkuPypi
import gradio as gr
import time

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit():
    info_window = "Out of credits..."
    path = 'no-credits.png'

    return info_window, path

def presentacionFinal(usuario, accion):

    print("Ent´re a presentación final....")
    print("La acción es: ", accion)
        
    #IMPORTANTE: Tienes que reconstruir capsule ahora que ya se obtiene del request, sino, capsule sera un State para el uso...
    #...de todos y es ahí donde radica el problema: 
    capsule = sulkuPypi.encripta(usuario).decode("utf-8") #decode es para quitarle el 'b
    
    if accion == "debita":        
        tokens = sulkuPypi.debitTokens(capsule, "picswap")
        info_window = "Image ready!"        
    else: 
        info_window = "No face in source path detected."
        tokens = gr.State.tokens

    
    html_credits = actualizar_creditos(tokens, usuario)       
    
    return html_credits, info_window

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