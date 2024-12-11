import importlib
import splashmix.configuracion
import os
import random

def randomNull(probabilidad, lista):
    # Generamos un número aleatorio entre 0 y 1
    numero_random = random.random()

    # Si la probabilidad es menor a 0.2 (20%), no guardamos el color
    if numero_random < probabilidad:
        result = None  #No habrá heroe.
    else:
        result = random.choice(lista)

    return result

def creadorObjeto(): 

    clase = getattr(importlib.import_module("splashmix.objetosCreacion"), splashmix.configuracion.creacion)
    creacion = clase()

    return creacion

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
    
    lista_archivos = os.listdir(ruta_carpeta)
    
    if not lista_archivos:
        print("La carpeta está vacía o no existe.")
        #FUTURE: Revisa si éste éxit corta el flujo y si eso es correcto.
        exit()

    #Selecciona una imagen aleatoriamente.
    posicion_aleatoria = random.choice(lista_archivos)
    ruta_posicion = os.path.join(ruta_carpeta, posicion_aleatoria)

    print("Ruta Posición seleccionada: ", ruta_posicion)    
    #nombre_archivo = os.path.basename(ruta_posicion)
    #shot, extension = nombre_archivo.split(".")
    #Ahora si necesitamos la extensión: 
    #shot = nombre_archivo
    #print("Posición elegida: ", shot)
        
    return ruta_posicion        

if __name__ == "__main__":
    getPosition()