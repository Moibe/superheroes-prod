#from data import usuarios
import gradio as gr
import sulkuPypi
import ast 

def authenticate(username, password):
    #Uno es el tiempo en que se tarda en obtener la cadena.
    cadena_usuarios = sulkuPypi.getData()    
    #Convertir la cadena en una lista de tuplas
    lista_usuarios = ast.literal_eval(cadena_usuarios)
    #Y otro el que se tarda en repasar la cadena.    
    for u, p in lista_usuarios:
        #Si el usuario y la contraseña son correctas...
        if username == u and password == p:
            print(f"{username} logged.")
            #Future, pensar como se va a corelacionar con login via Firebase.

            #Capsule es el usuario encriptado que enviarás a la API de Sulku.
            #capsule = sulkuPypi.encripta(username).decode("utf-8")
                                    
            return True

    #Si no hubo coincidencia regresas un false.    
    return False