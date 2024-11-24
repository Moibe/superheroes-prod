import bridges
import globales
import sulkuPypi
import sulkuFront
import gradio as gr
import gradio_client
import splash_tools
import time
import prompter
import tools

btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#PERFORM es la app INTERNA que llamará a la app externa.
def perform(input1, request: gr.Request):

    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    autorizacion = sulkuPypi.authorize(tokens, globales.work)
    if autorizacion is True:
        try: 
            resultado = mass(input1)
            #El resultado ya viene detuplado.
        except Exception as e:
            print("Mensaje de error al salir de MASS:", e)            
            info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = tools.titulizaExcepDeAPI(e))
            return resultado, info_window, html_credits, btn_buy          
    else:
        #Si no hubo autorización.
        info_window, resultado, html_credits = sulkuFront.noCredit(request.username)
        return resultado, info_window, html_credits, btn_buy
    
    #resultado_string = str(resultado)

    print("Result obtenido:")
    print(resultado)

    #Primero revisa si es imagen!: 
    if "image.webp" in resultado:
        #Si es imagen, debitarás.
        html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
    else: 
        #Si no es imagen es un texto que nos dice algo.
        info_window, resultado, html_credits = sulkuFront.aError(request.username, tokens, excepcion = resultado)
        return resultado, info_window, html_credits, btn_buy       
    
    #Éste solo aplica para astroblend, al parecer aquí no se usa así es que lo comentaré por el momento.
    #Revisión de errores PARTICULARES (textos propios de la app.)
    # if debit_rules.debita(resultado) == True:
    #     html_credits, info_window = sulkuFront.presentacionFinal(request.username, "debita")
    # else:
    #     html_credits, info_window = sulkuFront.presentacionFinal(request.username, "no debita") 
            
    #Lo que se le regresa oficialmente al entorno.
    return resultado, info_window, html_credits, btn_buy

#MASS es la que ejecuta la aplicación EXTERNA
def mass(input1):
    ("Entré a mass...")
    imagenSource = gradio_client.handle_file(input1)   
    print("Ésto es imagenSource después de ser procesada: ", imagenSource) 
    imagenPosition = gradio_client.handle_file(splash_tools.getPosition())     
    creacion=splash_tools.creadorObjeto()
    prompt = prompter.prompteador(creacion)   

    client = gradio_client.Client(globales.api, hf_token=bridges.hug)
    #client = gradio_client.Client("https://058d1a6dcdbaca0dcf.gradio.live/")  #MiniProxy
    
    print("Llegué a la ejecución de la API dentro de Mass:")
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
        
        result = splash_tools.desTuplaResultado(result)
        return result

    except Exception as e:
        print("Hubo un errora al ejecutar MASS:", e)
        print("Y el tipo de ese error es: ", type(e))
        #Errores al correr la API.
        #La no detección de un rostro es mandado aquí?! Siempre?
        mensaje = tools.titulizaExcepDeAPI(e)
        print("Mensaje de error:", e)
        
        return mensaje