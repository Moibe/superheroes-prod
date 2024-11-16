import ast 
import globales
import sulkuPypi

def authenticate(username, password):
    #Uno es el tiempo en que se tarda en obtener la cadena.
    cadena_usuarios = sulkuPypi.getData(globales.aplicacion)    
    #Convertir la cadena en una lista de tuplas
    lista_usuarios = ast.literal_eval(cadena_usuarios)
    #Y otro el que se tarda en repasar la cadena.    
    for u, p in lista_usuarios:
        #Si el usuario y la contraseña son correctas...
        if username == u and password == p:
            print(f"{username} logged.")
                                                
            return True

    #Si no hubo coincidencia regresas un False.    
    return False