import gradio as gr

app_path = "/superheroes-prod"
server_port=7800

#MAIN
version = "1.9.6 👾" #Reducción de quota aplica a usuario_proveedor.
firebase_auth = "dev" #o prod es si entrará al proyecto de dev(splashmix) o de prod(splashmix-ai) en firebase.

nombre_diccionario = "datos_superheroe"

#Aquí se elije el tipo de selección, no la api en si.
seleccion_api = "eligeQuotaOCosto" #eligeQuotaOCosto , eligeAOB o eligeGratisOCosto
max_size = 20

#Quota o Costo
api_zero = ("Moibe/InstantID2", "quota") #Indíca la url del api y su tipo.
api_cost = ("Moibe/InstantID2-B", "costo")

interface_api_name = "/generate_image" #El endpoint al que llamará client.

process_cost = 24

seto = "splashmix"
work = "picswap"
costo_work = 1 #Se integró costo_work para definir aquí directamente lo que cuesta picswap, y dejar de usar la var work.

tema = gr.themes.Base()
flag = "never"

neural_wait = 4
mensajes_lang = "es"

acceso = "login"  #login, metrado o libre, login para medición y acceso normal, metrado para no usar login pero si medir los créditos, para eso se utilizará el parámetro global de usuario, y libre no tiene login ni metrado.
usuario = "ella" #Ella se puede usar como el usuario infinito, por eso se deja libre.
credits_visibility = False

posicion_marker = False

proveedores = ['moibe', 'ss', 'bw', 'sun']