import time
import globales
import sulkuPypi
import gradio as gr

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit(usuario):
    info_window = "Out of credits..."
    path = 'images/no-credits.png'
    tokens = 0
    html_credits = visualizar_creditos(tokens, usuario)   

    return info_window, path, html_credits

def presentacionFinal(usuario, accion):

    print("La acción es: ", accion)
        
    #IMPORTANTE: Tienes que reconstruir capsule ahora que ya se obtiene del request, sino, capsule sera un State para el uso...
    #...de todos y es ahí donde radica el problema: 
    capsule = sulkuPypi.encripta(usuario).decode("utf-8") #decode es para quitarle el 'b
    
    if accion == "debita":        
        tokens = sulkuPypi.debitTokens(capsule, globales.work)
        info_window = "Image ready!"        
    else: 
        info_window = "No face in source path detected."
        tokens = sulkuPypi.getTokens(capsule)

    
    html_credits = visualizar_creditos(tokens, usuario)       
    
    return html_credits, info_window

def invisibiliza():
    return gr.Textbox(visible=bool(1)) 

def display_tokens(request: gr.Request):
 
    #getNovelty: userfile, aplicacion.
    novelty = sulkuPypi.getNovelty(sulkuPypi.encripta(request.username).decode("utf-8"), globales.aplicacion)
    
    if novelty == "new_user": 
        #Invisibiliza el display a los usuarios nuevos.
        display = gr.Textbox(visible=False)
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