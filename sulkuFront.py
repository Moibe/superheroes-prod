import time
import tools
import globales
import fireWhale
import threading
import gradio as gr
mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang) #import modulo_correspondiente

result_from_displayTokens = None 
result_from_initAPI = None    

def displayTokens(usuario):
    
    global result_from_displayTokens

    print("Entré a dipslay tokens, y ésto es usuario: ", usuario)

    #Obtengamos los datos hardcodeados del usuario mio, que no existe en las colecciones: 
    tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens')  
    #'5X8Hhd70uRclG1qfSJVj2zm211Q2' 
    novelty = fireWhale.obtenDato('usuarios', usuario, 'novelty' )
        
    if novelty == "new_user": 
        display = gr.Textbox(visible=False)
    else:
        tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens') 
        #tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
        display = visualizar_creditos(tokens, usuario) 
    
    result_from_displayTokens = display

def precarga(usuario_local, request: gr.Request):

    gr.Info(title="¡Bienvenido!", message=mensajes.lbl_info_welcome, duration=None)
    print("Ésto es el usuario_local: ", usuario_local)    

    
    # global result_from_initAPI
    # global result_from_displayTokens

    if globales.acceso == "login": 
        usuario = request.username
    else:        
        usuario = globales.usuario

    #thread1 = threading.Thread(target=initAPI)
    thread2 = threading.Thread(target=displayTokens, args=(usuario_local,))
    
    #thread1.start()
    thread2.start()

    #thread1.join()  # Espera a que el hilo 1 termine
    thread2.join()  # Espera a que el hilo 2 termine

    #return result_from_initAPI, result_from_displayTokens  
    return usuario_local 

def visualizar_creditos(nuevos_creditos, usuario):

    html_credits = f"""
    <div>
    <div style="text-align: left;">👤<b>{mensajes.lbl_username}: </b> {usuario}</div><div style="text-align: right;">💶<b>{mensajes.lbl_credits}: </b> {nuevos_creditos}</div>
    </div>
                    """    
     
    return html_credits

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit():
    info_window = sulkuMessages.out_of_credits
    path = 'images/no-credits.png'
    return path, info_window 

def aError(excepcion):
    info_window = manejadorExcepciones(excepcion)
    path = 'images/error.png'
      
    return path, info_window

def manejadorExcepciones(excepcion):
    #El parámetro que recibe es el texto despliega ante determinada excepción:
    if excepcion == "PAUSED": 
        info_window = sulkuMessages.PAUSED
    elif excepcion == "RUNTIME_ERROR":
        info_window = sulkuMessages.RUNTIME_ERROR
    elif excepcion == "STARTING":
        info_window = sulkuMessages.STARTING
    elif excepcion == "HANDSHAKE_ERROR":
        info_window = sulkuMessages.HANDSHAKE_ERROR
    elif excepcion == "GENERAL":
        info_window = sulkuMessages.GENERAL
    elif excepcion == "NO_FACE":
        info_window = sulkuMessages.NO_FACE
    elif excepcion == "NO_FILE":
        info_window = sulkuMessages.NO_FILE
    elif excepcion == "NO_POSITION": #Solo aplíca para Splashmix.
        info_window = sulkuMessages.NO_POSITION
    elif "quota" in excepcion: #Caso especial porque el texto cambiará citando la cuota.
        info_window = excepcion
    else:
        info_window = sulkuMessages.ELSE

    return info_window

def evaluaResultadoUsuario(resultado, personaje): 

    if "image.webp" in resultado:
        #Si es imagen, debitarás.
        resultado = tools.renombra_imagen(personaje, resultado)
        #accion = "no-debitar" if globales.acceso == "libre" else "debita"
        info_window = sulkuMessages.result_ok
    else: #CUANDO NO TRAE IMAGEN EL ERROR QUE PODRÍA TRAER ES NO_FACE O GENERAL (y ambos significarían que no detecto rostro).
        #Si no es imagen es un texto que nos dice algo.
        resultado, info_window = aError(excepcion = resultado)
        return resultado, info_window         
           
    return resultado, info_window
    