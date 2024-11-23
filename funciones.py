import bridges
import globales
import sulkuPypi
import sulkuFront
import debit_rules
import gradio as gr
import gradio_client
import splash_tools
import time
import prompter
import tools
import ast

btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#PERFORM es la app INTERNA que llamará a la app externa.
def perform(input1, request: gr.Request):

    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    autorizacion = sulkuPypi.authorize(tokens, globales.work)
    if autorizacion is True:
        try: 
            resultado = mass(input1)
        except Exception as e:            
            info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = tools.apicomProcessor(e))
            print("LLEGUÉ POR LA VIA DE EXCEPECION POR FALLA EN LA API.")
            return resultado, info_window, html_credits, btn_buy          
    else:
        info_window, resultado, html_credits = sulkuFront.noCredit(request.username)
        return resultado, info_window, html_credits, btn_buy
    
    resultado_string = str(resultado)

    print("LLEGUÉ A LA ZONA DE QUE SI RECIBÏ RESULTADO...")
    
    #Revisión de errores GENERALES (en cualquier API de HF):
    if "quota" in resultado_string: #Resultado_string porque no puede aplicar ésto en un tipo excepción.
        info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = resultado)
        print("Si entré a quota y estoy mandando su return.")
        return resultado, info_window, html_credits, btn_buy
    elif resultado == "HANDSHAKE_ERROR":
        info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = resultado)
        return resultado, info_window, html_credits, btn_buy
    elif resultado == "GENERAL": #Ya que incluimos que errores generales pueden llegar aquí, Handshake pordías quitarlo,
        #porque el comportamiento que debe de tener es general.
        info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = resultado)
        return resultado, info_window, html_credits, btn_buy
        
    #Revisión de errores PARTICULARES (textos propios de la app.)
    if debit_rules.debita(resultado) == True:
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
    else:
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "no debita") 
            
    #Lo que se le regresa oficialmente al entorno.
    return resultado, info_window, html_credits, btn_buy

#MASS es la que ejecuta la aplicación EXTERNA
def mass(input1):

    imagenSource = gradio_client.handle_file(input1)    
    imagenPosition = gradio_client.handle_file(splash_tools.getPosition())     
    creacion=splash_tools.creadorObjeto()
    prompt = prompter.prompteador(creacion)   

    client = gradio_client.Client(globales.api, hf_token=bridges.hug)
    #client = gradio_client.Client("https://058d1a6dcdbaca0dcf.gradio.live/")  #MiniProxy
        
    try:        
        result = client.predict(
                imagenSource,
                imagenPosition,
                prompt=prompt,
                negative_prompt="(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, pet collar, gun, weapon, 3d, drones, drone, buildings in background",
                style_name="(No style)", #ver lista en styles.txt
                num_steps=30,
                identitynet_strength_ratio=0.8,
                adapter_strength_ratio=0.8,
                #pose_strength=0.4,
                canny_strength=0.4,
                depth_strength=0.4,
                controlnet_selection=["depth"], #pueden ser ['pose', 'canny', 'depth'] #Al parecer pose ya no.
                guidance_scale=5,
                seed=42, 
                scheduler="EulerDiscreteScheduler",
                enable_LCM=False,
                enhance_face_region=True,
                api_name="/generate_image"
        )

        # result = client.predict(
		# p="Full Body",
		# api_name="/generate"
        # )
        # print(result)

        #CON MINIPROXY
        # result = client.predict(
		# input1=gradio_client.handle_file('https://raw.githubusercontent.com/gradio-app/gradio/main/test/test_files/bus.png'),
		# api_name="/predict"
        # )

        # #Si viene del miniproxy, hay que rehacer la tupla.
        # result = ast.literal_eval(result)        

        print("El result del predict es: ", result)
        result = splash_tools.procesaResultado(result)
        print(result)
        return result

    except Exception as e:
        print("Hubo un error:", e)
        print("Y el tipo de ese error es: ", type(e))
        #Errores al correr la API.
        mensaje = tools.apicomProcessor(e)
        return mensaje