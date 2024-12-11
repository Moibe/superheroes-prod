import os
import random
import importlib
import splashmix.configuracion
import time

def creadorObjeto():
    #Regresa un objeto creación con sus características.
    
    #De objetosCreación, importa el que indique splashmix.configuración:
    clase = getattr(importlib.import_module("splashmix.objetosCreacion"), splashmix.configuracion.creacion)
    
    #Crea ese objeto para regresarlo.    
    #AQUÏ ES DONDE ENTRA!!! DONDE SE LLAMA A HOTGIRL!!!! AQUÏ PODRÏAS PASAR EL PARAM!!
    creacion = clase() #Podrías agregar parametros para que así sea hecho desde su concepción: style="anime", adjective="naughty"
    #Pero por ahora se ponen de forma fija hasta después de creado. 
    #Future: Checar si cambiarlo a éste punto mejora rendimiento.
    return creacion

def randomNull(probabilidad, lista):
    # Generamos un número aleatorio entre 0 y 1
    numero_random = random.random()
    # Si la probabilidad es menor a 0.2 (20%), no guardamos el color
    if numero_random < probabilidad:
        result = ""  #No habrá dicho atributo. Antes ponía None, pero ahora "" para no afectar cuando genera texto para prompt.
    else:
        result = random.choice(lista) #Si eligirá un atributo de la lista.
    return result

def getPosition():
    """
    Regresa una posición del cuerpo humano para ser utilizada por el proceso de Stable Diffusion.

    Parameters:
    dataframe (dataframe): El dataframe en el que estuvimos trabajando.

    Returns:
    bool: True si se guardó el archivo correctamente.
    """
    #FUTURE: Aquí se podrá poner dinámicamente el set de posiciones en el subfolder de la carpeta posiciones.
    #Dentro de globales podemos poner subsets, después, asociarlos a determinados modelos.
    ruta_carpeta = os.path.join("images", "positions", splashmix.configuracion.positions_path)
    print("Ruta carpeta es: ", ruta_carpeta)
    
    try: 
        lista_archivos = os.listdir(ruta_carpeta)
        print("Lista archivos es: ", lista_archivos)
        #Selecciona una imagen aleatoriamente.
        posicion_aleatoria = random.choice(lista_archivos)
        ruta_posicion = os.path.join(ruta_carpeta, posicion_aleatoria)
        print("Ruta Posición seleccionada: ", ruta_posicion)
        return ruta_posicion     
    except Exception as e: 
        print("No hay carpeta de posiciones:", e)
        return e   

if __name__ == "__main__":
    getPosition()