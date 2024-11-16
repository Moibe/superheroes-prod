import bridges
import globales
import sulkuPypi
import sulkuFront
import debit_rules
import gradio as gr
import gradio_client
import time

abrazo = bridges.hug
btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#PERFORM es la app INTERNA que llamará a la app externa.
def perform(input1, request: gr.Request, *args):

    #Future: Maneja una excepción para el concurrent.futures._base.CancelledError
    #Future: Que no se vea el resultado anterior al cargar el nuevo resultado!         

    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), )
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    autorizacion = sulkuPypi.authorize(tokens, globales.work)
    if autorizacion is True:
        #IMPORTANTE: EJECUCIÓN DE LA APP EXTERNA: mass siempre será la aplicación externa que consultamos via API.   
        #resultado = mass(input1,input2)
        resultado = mass(input1, *args)
    else:
        info_window, resultado, html_credits = sulkuFront.noCredit(request.username)
        return resultado, info_window, html_credits, btn_buy
    
    #**SE EJECUTA EL LLAMADO Y OFRECE UN RESULTADO.**
    
    #2: ¿El resultado es debitable?
    if debit_rules.debita(resultado) == True:
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
    else:
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "no debita") 
            
    #Lo que se le regresa oficialmente al entorno.
    return resultado, info_window, html_credits, btn_buy

#MASS es la que ejecuta la aplicación EXTERNA
def mass(input1, input2): 

    imagenSource = gradio_client.handle_file(input1) 
    imagenDestiny = gradio_client.handle_file(input2)       

    client = gradio_client.Client(globales.api, hf_token=abrazo)
    result = client.predict(imagenSource, imagenDestiny, api_name="/predict")

    return result

def mass_zhi(input1, input2): 

    imagenSource = gradio_client.handle_file(input1) 
    #imagenDestiny = gradio_client.handle_file(input2)       

    client = gradio_client.Client(globales.api)
    #result = client.predict(imagenSource, imagenDestiny, api_name="/predict")

    result = client.predict(
		prompt="A hot girl in sexy cocktail dress topless.",
		person_img=imagenSource,
		seed=486992,
		randomize_seed=False,
		height=1024,
		width=1024,
		api_name="/character_gen"
        )
    
    print(result)
    print(result[0])
    

    return result[0]