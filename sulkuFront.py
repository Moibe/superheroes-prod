import globales
import sulkuPypi
import gradio as gr
import gradio_client
import bridges
import tools
import threading
from huggingface_hub import HfApi

result_from_displayTokens = None

def initAPI():
    #PROCESO1
    global result_from_initAPI

    try:
        repo_id = globales.api
        api = HfApi(token=bridges.hug)
        runtime = api.get_space_runtime(repo_id=repo_id)
        print("Hardware: ", runtime.hardware)
        print("Stage: ", runtime.stage)
        #"RUNNING_BUILDING", "APP_STARTING", "SLEEPING", "RUNNING"
        if runtime.stage == "SLEEPING":
            print("Estoy durmiendo..., Despierta")
            api.restart_space(repo_id=repo_id)
            print("Desperando")
        print("Hardware: ", runtime.hardware)
        # #"cpu-basic"
        
        # client = gradio_client.Client(globales.api, hf_token=bridges.hug)
        # print("Éste cliente: ", client.api_url)
        result_from_initAPI = runtime.stage
        # client = None
    except Exception as e:
        print("No api, encendiendo: ", e)
        result_from_initAPI = str(e)    
    
    print("API Result displayed: ", result_from_initAPI)   

def displayTokens(request: gr.Request):
    #PROCESO2
    print("Running displayTokens...")
    novelty = sulkuPypi.getNovelty(sulkuPypi.encripta(request.username).decode("utf-8"), globales.aplicacion)    
    if novelty == "new_user": 
        display = gr.Textbox(visible=False)
    else: 
        tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
        display = visualizar_creditos(tokens, request.username) 

    global result_from_displayTokens
    result_from_displayTokens = display
    print("Tokens displayed: ", result_from_displayTokens) 


def precarga(request: gr.Request):
    
    global result_from_initAPI
    global result_from_displayTokens

    thread1 = threading.Thread(target=initAPI)
    thread2 = threading.Thread(target=displayTokens, args=(request,))

    thread1.start()
    thread2.start()

    thread1.join()  # Espera a que el hilo 1 termine
    thread2.join()  # Espera a que el hilo 2 termine

    return result_from_initAPI, result_from_displayTokens  
    
  

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
    info_window = tools.manejadorExcepciones(excepcion)
    path = 'images/error.png'
    tokens = tokens
    html_credits = visualizar_creditos(tokens, usuario)   
    return info_window, path, html_credits

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