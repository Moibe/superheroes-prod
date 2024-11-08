#from data import usuarios
import gradio as gr
import sulkuPypi
import ast 

def authenticate(username, password):        

    cadena_usuarios = sulkuPypi.getData()    
    #Convertir la cadena en una lista de tuplas
    lista_usuarios = ast.literal_eval(cadena_usuarios)        
        
    for u, p in lista_usuarios:
        #Si el usuario y la contraseña son correctas...
        if username == u and password == p:
            #Future, pensar como se va a corelacionar con login via Firebase.

            #Capsule es el usuario encriptado que enviarás a la API de Sulku.
            #El encriptador ahora será parte de Sulku, porque es una herramienta que se requiere para...
            #...las comunicaciones con Sulku.
            capsule = sulkuPypi.encripta(username).decode("utf-8") #decode es para quitarle el 'b
     
            #Checa cuantos tokens tiene ese usuario via la API de Sulku: 
            #FUTURE: Checa si vale la pena guardar éstos estados.
            gr.State.tokens = sulkuPypi.getTokens(capsule)
                                    
            return True

    #Si no hubo coincidencia regresas un false.    
    return False