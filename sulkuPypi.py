import time
import bridges
import globales
import requests
from cryptography.fernet import Fernet

#Sulkupypi será el que en un futuro se volverá un paquete de python que instalarás y en el futuro quizá comercializarás.

base_url = "https://moibe-sulku-fastapi-docker.hf.space/"
#userfile = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="
#Ojo, cuando el userfile termina con símbolo igual y supongo que también si empieza, causa problemas, la solución, ...
#... implementar más adelante desde ser agregar un caractér delimitador y despúes quitarlo, esto para evitar problemas...
#... con el símbolo =, ? y &. Dicho problema solo sucede cuando lo recibe como query params no como path params.
work = globales.work

#Todas son llamadas a la API, excepto encripta, que es una herramienta para prepara precisamente, ...
#lo que le vas a enviar a la API.
def encripta(username):

    key = bridges.key
    fernet = Fernet(key)
    string_original = username
    string_encriptado = fernet.encrypt(string_original.encode("utf-8"))

    # string_desencriptado = fernet.decrypt(string_encriptado).decode("utf-8")
    # print("String original:", string_original)
    # print("String encriptado:", string_encriptado)
    # print("String desencriptado:", string_desencriptado)

    return string_encriptado

def getData():
    #Obtiene la lista de usuarios para brindar o no brindar acceso. 
    method = "getData/"
    api_url = base_url + method

    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        data = response.json()

    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return data

def getNovelty(userfile):

    method = "getUserNovelty/"
    params = userfile

    api_url = base_url + method + params
    print("Usando la api_url: ", api_url)
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        novelty = response.json()

        print("Esto es la flag de novelty obtenida: ", novelty)
        return novelty
              
    else:
        print("Error al obtener el elemento todo:", response.status_code)
        return "f{error:}"
    

def getTokens(userfile):

    method = "getTokens/"
    params = userfile
    
    api_url = base_url + method + params
    print("En getTokens la api_url que estoy usando es: ", api_url)
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
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

def debitTokens(userfile, work):

    method = "debitTokens/"
    params = userfile + "/" + work

    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

def debitTokensQ(userfile, work):

    #debitTokens pero con QueryParams, (los query params sirve para ocasiones en los que usas dos de un mismo query param para abtener el resultado de un AND o rangos como...
    #... clima por ejemplo.)
    method = "debitTokens?"
    params = "userfile=" + userfile + "&" + "work=" +  work

    api_url = base_url + method + params
    response = requests.get(api_url)

    if response.status_code == 200:
        print("Conexión a Sulku successful...")
        tokens = response.json()
        print("Tokens:", tokens)
    else:
        print("Error al obtener el elemento todo:", response.status_code)

    return tokens

if __name__ == "__main__":
    getTokens(userfile)
    authorize(18, globales.work)
    debitTokens(userfile, work)