import globales
import sulkuPypi
import gradio as gr
import gradio_client
import bridges
import tools
import threading
from huggingface_hub import HfApi

result_from_displayTokens = None 
result_from_initAPI = None    

def displayTokens(request: gr.Request):
    
    global result_from_displayTokens

    print("Running displayTokens...")
    novelty = sulkuPypi.getNovelty(sulkuPypi.encripta(request.username).decode("utf-8"), globales.aplicacion)    
    if novelty == "new_user": 
        display = gr.Textbox(visible=False)
    else: 
        tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
        display = visualizar_creditos(tokens, request.username) 
    
    result_from_displayTokens = display

def precarga(request: gr.Request):
    
    # global result_from_initAPI
    # global result_from_displayTokens

    #thread1 = threading.Thread(target=initAPI)
    thread2 = threading.Thread(target=displayTokens, args=(request,))

    #thread1.start()
    thread2.start()

    #thread1.join()  # Espera a que el hilo 1 termine
    thread2.join()  # Espera a que el hilo 2 termine

    #return result_from_initAPI, result_from_displayTokens  
    return result_from_displayTokens 

def visualizar_creditos(nuevos_creditos, usuario):

    html_credits = f"""
    <div>
    <div style="text-align: left;">👤<b>Username: </b> {usuario}</div><div style="text-align: right;">💶<b>Credits Available: </b> {nuevos_creditos}</div>
    </div>
                    """    
     
    return html_credits

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit(usuario):
    info_window = "Out of credits..."
    path = 'images/no-credits.png'
    tokens = 0
    html_credits = visualizar_creditos(tokens, usuario)
    return info_window, path, html_credits

def aError(usuario, tokens, excepcion):
    #aError se usa para llenar todos los elementos visuales en el front.
    info_window = manejadorExcepciones(excepcion)
    path = 'images/error.png'
    tokens = tokens
    html_credits = visualizar_creditos(tokens, usuario)   
    return info_window, path, html_credits

def manejadorExcepciones(excepcion):
    #El parámetro que recibe es el texto despliega ante determinada excepción:
    if excepcion == "PAUSED": 
        info_window = "AI Engine Paused, ready soon."
    elif excepcion == "RUNTIME_ERROR":
        info_window = "Error building AI environment, please contact me."
    elif excepcion == "STARTING":
        info_window = "Server Powering UP, wait a few minutes and try again."
    elif excepcion == "HANDSHAKE_ERROR":
        info_window = "Connection error try again."
    elif excepcion == "GENERAL":
        info_window = "Network error, no credits were debited."
    elif excepcion == "NO_FACE":
        info_window = "Unable to detect a face in the image. Please upload a different photo with a clear face."
    elif excepcion == "NO_FILE":
        info_window = "No file, please add a valid archive."
    elif "quota" in excepcion: #Caso especial porque el texto cambiará citando la cuota.
        info_window = excepcion
    else:
        info_window = "Error. No credits were debited."

    return info_window

def presentacionFinal(usuario, accion):
        
    capsule = sulkuPypi.encripta(usuario).decode("utf-8") #decode es para quitarle el 'b
    
    if accion == "debita":        
        tokens = sulkuPypi.debitTokens(capsule, globales.work, globales.env)
        info_window = "Image ready!"        
    else: 
        info_window = "No face in source path detected."
        tokens = sulkuPypi.getTokens(capsule, globales.env)
    
    html_credits = visualizar_creditos(tokens, usuario)       
    
    return html_credits, info_window