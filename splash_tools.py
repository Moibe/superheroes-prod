import importlib
import configuracion.globales
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

    clase = getattr(importlib.import_module("objetosCreacion"), configuracion.globales.creacion)
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
    ruta_carpeta = os.path.join("images", "groupBatch")
    #FUTURE que también arrojé sin posición.

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

def procesaResultado(resultado):
    #PROCESO DESPÚES DE QUE YA TERMINÓ EL STABLE DIFUSSE:
    #SI PROCESO CORRECTAMENTE SERÁ UNA TUPLA.        
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
        

if __name__ == "__main__":
    getPosition()