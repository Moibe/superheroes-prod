import random
import gradio as gr
import globales
from huggingface_hub import HfApi
import bridges
import sulkuPypi
import time

def theme_selector():
    temas_posibles = [
        gr.themes.Base(),
        gr.themes.Default(),
        gr.themes.Glass(),
        gr.themes.Monochrome(),
        gr.themes.Soft()
    ]
    tema = random.choice(temas_posibles)
    #print("Tema random: ", tema)
    return tema

def initAPI(api):
    
    global result_from_initAPI

    try:
        repo_id = api
        llave = HfApi(token=bridges.hug)
        runtime = llave.get_space_runtime(repo_id=repo_id)
        print("Stage: ", runtime.stage)
        #"RUNNING_BUILDING", "APP_STARTING", "SLEEPING", "RUNNING", "PAUSED", "RUNTIME_ERROR"
        if runtime.stage == "SLEEPING":
            llave.restart_space(repo_id=repo_id)
            print("Despertando")
        print("Hardware: ", runtime.hardware)
        result_from_initAPI = runtime.stage

    except Exception as e:
        #Creo que ya no debería de llegar aquí.
        print("No api, encendiendo: ", e)
        result_from_initAPI = str(e)    
    
    return result_from_initAPI

def titulizaExcepDeAPI(e):  
    #Resume una excepción a un título manejable.
    if "RUNTIME_ERROR" in str(e):
        resultado = "RUNTIME_ERROR" #api mal construida tiene error.
    elif "PAUSED" in str(e):
        resultado = "PAUSED" 
    elif "The read operation timed out" in str(e): #IMPORTANTE, ESTO TAMBIÉN SUCEDE CUANDO LA DESPIERTAS Y ES INSTANTÁNEO.
        resultado = "STARTING"
    elif "GPU quota" in str(e): 
        resultado = recortadorQuota(str(e)) #Cuando se trata de quota regresa el resultado completo convertido a string.
    elif "handshake operation timed out" in str(e):
        resultado = "HANDSHAKE_ERROR"
    elif "File None does not exist on local filesystem and is not a valid URL." in str(e):
        resultado = "NO_FILE"
    #A partir de aquí son casos propios de cada aplicación.
    elif "Unable to detect a face" in str(e):
        resultado = "NO_FACE"
    elif "positions" in str(e):
        resultado = "NO_POSITION"
    else: 
        resultado = "GENERAL"

    return resultado
    
def recortadorQuota(texto_quota):
    # Encontrar el índice de inicio (después de "exception:")
    indice_inicio = texto_quota.find("exception:") + len("exception:")
    # Encontrar el índice de final (antes de "<a")
    indice_final = texto_quota.find("<a")
    
    if indice_final == -1: #Significa que no encontró el texto "<a" entonces buscará Sign-Up.
        indice_final = texto_quota.find("Sign-up")
    
    #Extraer la subcadena
    subcadena = texto_quota[indice_inicio:indice_final]

    #Y si el objetivo es nunca desplegar el texto Hugging Face, éste es el plan de escape final.
    if "Hugging" in subcadena: 
        nuevo_mensaje = "Your quota is exceeded, try again in few hours please."
        return nuevo_mensaje
    else:
        print(subcadena)
    
    return subcadena

def desTuplaResultado(resultado):
    #Procesa la tupla recibida y la convierte ya sea en imagen(path) o error(string)       
    if isinstance(resultado, tuple):

        print("El resultado fue una tupla, ésta tupla:")
        print(resultado)
        ruta_imagen_local = resultado[0]
        print("Ésto es resultado ruta imagen local: ", ruta_imagen_local)
        return ruta_imagen_local       

    #NO PROCESO CORRECTAMENTE NO GENERA UNA TUPLA.
    #CORRIGE IMPORTANTE: QUE NO SE SALGA DEL CICLO DE ESA IMAGEN AL ENCONTRAR ERROR.
    else:
        #NO ES UNA TUPLA:
        print("El tipo del resultado cuando no fue una tupla es: ", type(resultado))                
        texto = str(resultado)
        segmentado = texto.split('exception:')
        print("Segmentado es una posible causa de error, analiza segmentado es: ", segmentado)
        #FUTURE: Agregar que si tuvo problemas con la imagen de referencia, agregue en un 
        #Log de errores porque ya no lo hará en el excel, porque le dará la oportunidad con otra 
        #imagen de posición.
        try:
            #Lo pongo en try porque si no hay segmentado[1], suspende toda la operación. 
            print("Segmentado[1] es: ", segmentado[1])
            mensaje = segmentado[1]
            return mensaje
        except Exception as e:
            print("Error en el segmentado: ", e)
            # mensaje = "concurrent.futures._base.CancelledError"
            # concurrents = concurrents + 1
        finally: 
            pass

def elijeAPI():

    diferencia = sulkuPypi.getQuota() - globales.process_cost
    
    if diferencia >= 0:
        #Puedes usar Zero.
        api = globales.api_zero
        tipo_api = "gratis"
        #Además Si el resultado puede usar la Zero "por última vez", debe de ir prendiendo la otra.
        #if diferencia es menor que el costo de un sig.  del proceso, ve iniciando ya la otra API.
        if diferencia < globales.process_cost:
            print("Preventivamente iremos prendiendo la otra.")
            initAPI(globales.api_cost) 
    else:
        api = globales.api_cost
        tipo_api = "costo"

    print("La API elegida es: ", api)
    
    return api, tipo_api