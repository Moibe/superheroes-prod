import tools
import random
import bridges
import globales
import fireWhale
import sulkuFront
import gradio as gr
import gradio_client
import splashmix.prompter as prompter
import splashmix.splash_tools as splash_tools
import splashmix.configuracion as configuracion
mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang)
import time

btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#PERFORM es la app INTERNA que llamará a la app externa.
def perform(input1, gender, personaje, usuario):

    gender = gender or "superhero" #default es superhero.
    #Los tokens se checan dentro de perform para estar seguros de que cuenta con los tokens para ejecutar esa operación en particular.
    tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens')
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    if tokens >= globales.costo_work: 
        try:            
            resultado = mass(input1, gender, personaje)
        except Exception as e:      
            resultado, info_window  = sulkuFront.aError(excepcion = tools.titulizaExcepDeAPI(e))
            return resultado, info_window          
    else:
        #Si no hubo autorización.
        resultado, info_window = sulkuFront.noCredit()
        return resultado, info_window

    #AQUÍ LLEGARA CUANDO NO ES ERROR DE SISTEMA Y ES DE USUARIO (O LOGRO LA IMAGEN O PUSO UNA SIN ROSTRO DETECTABLE)
    resultado, info_window = sulkuFront.evaluaResultadoUsuario(resultado, personaje) #No fue frenado por falta de crédito o or imagen vacía, paso a la API (se debita)
    return resultado, info_window

#MASS es la que ejecuta la aplicación EXTERNA
def mass(input1, gender, hero):

    print("Estoy en MASS....")
        
    #Al parecer la API se elige hasta perform, basado en lo que se especifico en globales.
    api, tipo_api = tools.eligeAPI(globales.seleccion_api) 
    print(f"De vuelta en mass la api elegida es {api} y el tipo es {tipo_api}...") 
    client = gradio_client.Client(api, hf_token=bridges.hug)
    
    #Adquisición Databank Particular para ese objeto y género....
    nombre_databank = gender
    datos = getattr(configuracion, nombre_databank)
    
    #Posición
    imagenSource = gradio_client.handle_file(input1)
    carpeta_positions = datos["positions_path"]  
    imagenPosition = gradio_client.handle_file(splash_tools.getPosition(carpeta_positions)) 

    #nombre_posicion = imagenPosition['path']
    
    #Ésta parte es para obtener el nombre de la posición y guardarla en el log.
    #nombre_posicion = imagenPosition['path'].rsplit("\\", 1)[1] 
      
    #Objeto a Crear
    #creacion_seleccionada = datos["creacion"]
    #selected_databank = datos["selected_databank"] #Se usa cuando viene de objeto no de dropdown.
    #creacion=splash_tools.creadorObjeto(creacion_seleccionada, selected_databank) #Se usa solo si se arma como objeto random.
    #1) Aquí podrías pasarle style="anime".
    #2) Aquí con los parámetros que te estuviera pasando por ejemplo via input.
    #En éste ejemplo haríamos que siempre sea ánime. #creacion.style = "Anime"
    
    #Prompt, que también usará que objeto és y su género.
    #prompt = prompter.prompteador(creacion, gender)    
    #Fraseador se usa cuando traemos el que heroe es directo del dropdownlist.
    prompt = prompter.fraseador(hero, gender)

    try:     

        result = client.predict(
                imagenSource,
                imagenPosition,
                prompt=prompt,
                #negative_prompt="(lowres, low quality, worst quality:1.2), (text:1.2), watermark, (frame:1.2), deformed, ugly, deformed eyes, blur, out of focus, blurry, deformed cat, deformed, photo, anthropomorphic cat, monochrome, pet collar, gun, weapon, 3d, drones, drone, buildings in background",
                style_name="(No style)", #ver lista en styles.txt
                num_steps=30,
                identitynet_strength_ratio=0.8,
                adapter_strength_ratio=0.8,
                #pose_strength=0.4,
                canny_strength=0.4,
                depth_strength=0.4,
                controlnet_selection=["depth"], #pueden ser ['pose', 'canny', 'depth'] #Al parecer pose ya no.
                guidance_scale=5,
                seed=random.randint(0, 2147483647), 
                scheduler="EulerDiscreteScheduler",
                enable_LCM=False,
                enhance_face_region=True,
                api_name=globales.interface_api_name
        )

        #IMPORTANTE: cuando InstantID no detecta un rostro, no dice que eso fue el error. 
        #Así es que por ahora asumiré que la única forma en la que InstantID regresa error es porque no detecto un rostro...
        #Y de ahí partiré.  

        tools.reducirQuota(tipo_api) #Si estamos en sistema de quotas. Aplica un IF.
            
        result = tools.desTuplaResultado(result)
        return result

    except Exception as e:
        #La no detección de un rostro es mandado aquí?! Siempre? SI SIEMPRE, porque instantID es diferente y no reporta ese error integramente, pero aquí llega.
        mensaje = tools.titulizaExcepDeAPI(e)        
        return mensaje