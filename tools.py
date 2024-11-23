import random
import traceback
import gradio as gr

def theme_selector():
    temas_posibles = [
        gr.themes.Base(),
        gr.themes.Default(),
        gr.themes.Glass(),
        gr.themes.Monochrome(),
        gr.themes.Soft()
    ]
    tema = random.choice(temas_posibles)
    print("Tema random: ", tema)
    return tema

def titulizaExcepDeAPI(e):    
    #Resume una excepción a un título manejable.
    print("Except recibido por apicom: ", e)
    print("Traceback @ tools: Except recibido por apicom:")
    traceback.print_exc()
    tb = traceback.format_exc()
    print("Error en la línea", tb.split('\n')[-2].split(',')[1].strip())
    print("Mensaje de error:", e)
    
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
    elif "Unable to detect a face" in str(e):
        resultado = "NO_FACE"
    else: 
        resultado = "GENERAL"

    return resultado

def manejadorExcepciones(excepcion):
    #El parámetro que recibe es el texto despliega ante determinada excepción:
    if excepcion == "PAUSED": 
        info_window = "AI Engine Paused, ready soon."
    elif excepcion == "RUNTIME_ERROR":
        info_window = "Error in AI, please contact Moibe."
    elif excepcion == "STARTING":
        info_window = "Server Powering UP, wait a few seconds and try again."
    elif excepcion == "HANDSHAKE_ERROR":
        info_window = "Connection error try again."
    elif excepcion == "GENERAL":
        info_window = "Network error, no credits were debited."
    elif excepcion == "NO_FACE":
        info_window = "Unable to detect a face in the image. Please upload a different photo with a clear face."
    elif "quota" in excepcion: #Caso especial porque el texto cambiará citando la cuota.
        info_window = excepcion
    else:
        info_window = "Error. No credits were debited."

    return info_window
    
def recortadorQuota(texto_quota):
    # Encontrar el índice de inicio (después de "exception:")
    indice_inicio = texto_quota.find("exception:") + len("exception:")
    # Encontrar el índice de final (antes de "<a")
    indice_final = texto_quota.find("<a")
    print("EL INDICE FINAL ES: ", indice_final)
    # if indice_final == -1: #Significa que no encontró el texto "<a" entonces buscará Sign-Up.
    #     indice_final = texto_quota.find("Sign-up")
    # Extraer la subcadena
    subcadena = texto_quota[indice_inicio:indice_final]

    #Y si el objetivo es nunca desplegar el texto Hugging Face, éste es el plan de escape final.
    if "Hugging" in subcadena: 
        nuevo_mensaje = "Your quota is exceeded, try again in few hours please."
        return nuevo_mensaje
    else:
        print("El recorte quedó: ")
        print(subcadena)

        return subcadena