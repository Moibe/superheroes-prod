import inputs
import random
import globales
import funciones
import sulkuFront
import gradio as gr
import firehead, fire, fuego, aire, tierra, magma 
from huggingface_hub import login
import bridges

login(token=bridges.hug)

#import tools
#mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang)

def iniciar():    
    app_path = "/superheroes-prod"
    main.queue(max_size=globales.max_size)
    main.launch(root_path=app_path, server_port=globales.server_port)

#Credit Related Elements
html_credits = gr.HTML(visible=globales.credits_visibility)
lbl_console = gr.Label(label="AI Terminal " + globales.version +  " messages", value="Hola", container=True)
#btn_buy = gr.Button("Get Credits", visible=True, size='lg')

#Customizable Inputs and Outputs
input1, gender, personaje, result = inputs.inputs_selector(globales.seto)    

#Otros Controles y Personalizaciones
nombre_posicion = gr.Label(label="Posición", visible=globales.posicion_marker)

enviar_btn=gr.Button("Enviar", variant="primary"),
despejar_btn=gr.Button("Borrar", variant="secondary"),  

def tester(input1):
    print("Ésto es tester")

def welcome(usuario_firebase): 
    print("Esto es una prueba de welcome:", usuario_firebase)
    botones = ['huggingface', 'primary', 'secondary', 'stop']
    return gr.Button(value="Cerrar Sesión", size='md', variant=random.choice(botones))

#fire provee las partes de javascript que se requieren para correr el chequeo de firebase.
with gr.Blocks(theme=globales.tema, head=firehead.head, js=fire.js, css="footer {visibility: hidden}") as main:
    
    usuario_firebase = gr.Textbox(visible=False) #Espacio para almacenar el usuario de firebase 
    acheteemeele = gr.HTML(visible=False)

    with gr.Row(variant='compact', show_progress=False):
        with gr.Column():
            acordeon = gr.Accordion(label = "Splashmix IA", open=False)
            with acordeon:   
             btn_logout = gr.Button(value="Cerrar Sesión 👋🏻", size='lg', variant='primary')
        with gr.Column():
            acordeon2 = gr.Accordion(label = "Por favor refresca la página (F5)...", open=False)
            with acordeon2: 
                compra = gr.Button(value="Recargar Créditos ⚡", size='lg', variant='primary')
 
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[input1, gender, personaje, usuario_firebase], 
            outputs=[result, lbl_console], 
            flagging_mode=globales.flag,
            js=fuego.js,        
            )        
    
    result.change(sulkuFront.actualizador_navbar, [usuario_firebase, result, lbl_console], acordeon2)
    #gender.select(tester, input1, input1, js=fuego.js) #Ésto recarga los créditos por si no se logró al inicio.
    # compra.click(None, usuario_firebase, None, js=tierra.js)
    # btn_logout.click(welcome, usuario_firebase, btn_logout, js=aire.js)
    
    btn_logout.click(
            fn=welcome,  # Una función Python, aunque no haga nada relevante para la redirección
            inputs=[usuario_firebase],
            outputs=[],
            js=tierra.js
            )
    compra.click(
            fn=welcome,  # Una función Python, aunque no haga nada relevante para la redirección
            inputs=[usuario_firebase],
            outputs=[],
            js="() => window.location.href = 'https://app.splashmix.ink/buy'" 
        # Esta línea de JavaScript abre la URL en la misma pestaña
            )
    #print("Print antes de load? Usuario_firebase: ", usuario_firebase.value)
    main.load(sulkuFront.precarga, usuario_firebase, [usuario_firebase, acordeon, btn_logout, acordeon2], js=fuego.js) if globales.acceso != "libre" else None
iniciar()