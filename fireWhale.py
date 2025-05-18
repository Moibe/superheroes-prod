import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

from firebase_admin import auth

# Use the application default credentials.
cred = credentials.Certificate('config.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
#dato es el Documento que traes  como el nombre del user. 
#info es la info de ese dato que estás buscando, como token.
def obtenDato(coleccion, dato, info):
    print(f"Estoy dentro de obtenDato y los valores que recibí son: {coleccion}, {dato}, {info}...")
    time.sleep(3)
    #Primero debemos definir la referencia al documento, o sea a la hoja de usuario.
    doc_ref = db.collection(coleccion).document(dato) 
    print("El doc ref recibido es: ", doc_ref)

    #Éste es el documento que tiene los datos de ella.
    documento = doc_ref.get()
    

    if documento.exists:
        pass #El documento si existe.        
    else:
        print("No existe el documento, es un nuevo usuario.")
        creaDato(coleccion, dato, 'tokens', 5) #porque agregará 5 tokens.       
    
    #Recuerda la conversión a diccionario.
    documento = doc_ref.get() 
    diccionario = documento.to_dict()
    return diccionario.get(info)

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