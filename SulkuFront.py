import sulkuPypi
import gradio as gr
import time

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit(usuario):
    info_window = "Out of credits..."
    path = 'no-credits.png'
    tokens = gr.State.tokens
    print("Estoy en no-credit, no debería recalcular porque es cero, pero gr.State.tokens es: ", gr.State.tokens)
    #Importante, ojo con que si sirve gr.State.tokens
    html_credits = visualizar_creditos(tokens, usuario)   

    return info_window, path, html_credits

def presentacionFinal(usuario, accion):

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

    
    html_credits = visualizar_creditos(tokens, usuario)       
    
    return html_credits, info_window

def invisibiliza():
    return gr.Textbox(visible=bool(1)) 

def display_tokens(request: gr.Request):
   

    #Para desplegar o no desplegar, necesitamos saber si el usuario es new user.
    novelty = sulkuPypi.getNovelty(sulkuPypi.encripta(request.username).decode("utf-8"))
    print("La flag de novelty obtenida es: ", novelty)

    if novelty == "new_user": 
        print("INVISIBILIZA")
        display = gr.Textbox(visible=False)
        time.sleep(2)
    else: 
        tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"))
        display = visualizar_creditos(tokens, request.username)      
    
    return display

def visualizar_creditos(nuevos_creditos, usuario):

    html_credits = f"""
    <div>
    <div style="text-align: left;">👤<b>Username: </b> {usuario}</div><div style="text-align: right;">💶<b>Credits Available: </b> {nuevos_creditos}</div>
    </div>
                    """

    
     
    return html_credits