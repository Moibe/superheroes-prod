import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

from firebase_admin import auth

# Use the application default credentials.
cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

def obtenDatosUIDFirebase(uid):
    """
    Verifica si un UID existe en Firebase Authentication.
    Esto con el fin de evitar que se cambié el id arbitrareamente desde localstorage.

    Args:
        uid (str): El User ID (UID) que se desea verificar.

    Returns:
        bool: True si el usuario con ese UID existe, False en caso contrario.
    """
    try:
        # Intenta obtener el usuario por su UID
        #Todo usuario nuevo, si debería estar en auth porque previamente se registro ahí. 
        #Pero si es nuevo, no tendrá registro en firestore, cosa que haremos en python desde superheroes-prod
        user = auth.get_user(uid) #Obtengo el objeto con todos los datos.
        print("Ésto es el user obtenido de la comprobación: ", user)
        email = user.email
        displayName = user.display_name
        
        # Si la operación es exitosa, el usuario existe
        print(f"✔️ Usuario con UID '{uid}' encontrado en Firebase Auth: {user.email or 'sin email'}")
        return email, displayName 
    except auth.UserNotFoundError:
        # Esta excepción se lanza específicamente si el UID no existe
        print(f"❌ Usuario con UID '{uid}' NO encontrado en Firebase Auth.")
        return None, None
    except Exception as e:
        # Captura cualquier otro error (ej. problemas de conexión, permisos)
        print(f"❌ Error al verificar usuario con UID '{uid}': {e}")
        return None, None    

#dato es el Documento que traes  como el nombre del user. 
#info es la info de ese dato que estás buscando, como token.
def obtenDato(coleccion, dato, info):
    
    print(f"Estoy dentro de obtenDato y los valores que recibí son: {coleccion}, {dato}, {info}...")
    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(dato) 
    print("El doc ref recibido es: ", doc_ref)

    #Éste es el documento que tiene los datos de ella.
    documento = doc_ref.get()
    print("Esto es el documento obtenido: ", documento)
      
    #Quizá éste segmento que comenté era el que producia nuevos documentos sin deber.
    if documento.exists:
        print("El documento existe....")
        #Recuerda la conversión a diccionario.
        documento = doc_ref.get() 
        diccionario = documento.to_dict()
        print("Esto es el diccionario: ", diccionario)
        resultado = diccionario.get(info)
        print("Éste es el resultado...", resultado)
        return resultado
        pass #El documento si existe.        
    else:
        print("No existe el documento, es un nuevo usuario.")
        return None
        #No crees nada pero avisa que no existe.
        #creaDato(coleccion, dato, 'tokens', 5) #porque agregará 5 tokens.

def editaDato(coleccion, dato, info, contenido):

    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(dato)
    
    doc_ref.update({
        # 'quote': quote,
        info: contenido,
    })

def creaDato(coleccion, dato, info, contenido):

    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(dato)
    
    doc_ref.set({
        # 'quote': quote,
        info: contenido,
    })

def creaDatoMultiple(coleccion, dato, data_dict):
    """
    Crea un nuevo documento o sobrescribe uno existente en Firestore
    con múltiples pares de campo-contenido.

    Args:
        coleccion (str): El nombre de la colección donde se creará/actualizará el documento.
        dato (str): El ID del documento que se va a crear o sobrescribir.
        data_dict (dict): Un diccionario donde las claves son los nombres de los campos
                          y los valores son el contenido de esos campos.
                          Ej: {'nombre': 'Juan', 'edad': 30, 'activo': True}
    """
    # Primero definimos la referencia al documento
    doc_ref = db.collection(coleccion).document(dato)
    
    try:
        # Usamos .set() y le pasamos el diccionario completo.
        # Esto sobrescribirá el documento si ya existe con los nuevos datos.
        doc_ref.set(data_dict)
        
        print(f"✔️ Documento '{dato}' creado/sobrescrito en la colección '{coleccion}' con los siguientes datos:")
        for key, value in data_dict.items():
            print(f"  - {key}: {value}")
            
    except Exception as e:
        print(f"❌ Error al crear/sobrescribir documento '{dato}' en '{coleccion}': {e}")

def verificar_token(id_token):
    """Verifica el token de ID de Firebase."""
    try:
        # Verifica el token y decodifica la información del usuario
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        return uid  # Retorna el UID del usuario si el token es válido
    except auth.InvalidIdTokenError as e:
        print(f"Token inválido: {e}")
        return None  # Retorna None si el token es inválido