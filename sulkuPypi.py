import time
import bridges
import globales
import requests
from cryptography.fernet import Fernet

#Sulkupypi será el que en un futuro se volverá un paquete de python que instalarás y en el futuro quizá comercializarás.

base_url = "https://moibe-sulku-fastapi-docker.hf.space/"
work = globales.work

#Todas son llamadas a la API, excepto encripta, que es una herramienta para prepara precisamente, ...
#lo que le vas a enviar a la API.
def encripta(username):

    key = bridges.key
    fernet = Fernet(key)
    string_original = username
    string_encriptado = fernet.encrypt(string_original.encode("utf-8"))

    return string_encriptado

def getData(aplicacion):
    #Obtiene la lista de usuarios para brindar o no brindar acceso. 
    method = "getData/"
    params = aplicacion
    api_url = base_url + method + params

    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        data = response.json()

    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return data

def getNovelty(userfile, aplicacion):

    method = "getUserNovelty/"
    params = userfile + "/" + aplicacion

    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        novelty = response.json()

        print("Esto es la flag de novelty obtenida: ", novelty)
        return novelty
              
    else:
        print("Error al obtener el elemento todo:", response.status_code)
        return "f{error:}"
    

def getTokens(userfile, env):

    method = "getTokens/"
    params = userfile + "/" + env
    
    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

def authorize(tokens, work):

    method = "authorize/"
    params = str(tokens) + "/" + work

    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        autorizacion = response.json()
        print("Autorización:", autorizacion)        
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return autorizacion

def debitTokens(userfile, work, env):

    method = "debitTokens/"
    params = userfile + "/" + work + "/" + env

    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        #print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

def debitTokensQ(userfile, work, env):

    #debitTokens pero con QueryParams, (los query params sirve para ocasiones en los que usas dos de un mismo query param para obtener el resultado de un AND o rangos como...
    #... clima por ejemplo.)
    method = "debitTokens?"
    #Y como puedes ver el armado de sus params es dintinto ya que usa ampersand &
    params = "userfile=" + userfile + "&" + "work=" +  work + "&" + env

    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

if __name__ == "__main__":
    #params: aplicacion
    getData(globales.aplicacion)
    #params: userfile, aplicacion
    getNovelty(globales.sample_userfile, globales.aplicacion)
    #params: userfile, env
    getTokens(globales.sample_userfile, globales.env)
    #params: tokens, work
    authorize(18, globales.work)
    #params: userfile, work
    debitTokens(globales.sample_userfile, globales.work, globales.env)