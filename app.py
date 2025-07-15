import inputs
import globales
import funciones
import sulkuFront
import gradio as gr
import firehead, fire, fuego, aire 
import random
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
            acordeon = gr.Accordion(open=False)
            with acordeon:   
             btn_logout = gr.Button(value="Cerrar Sesión 👋🏻", size='lg', link="https://buy.splashmix.ink", variant='primary')
        with gr.Column():
            acordeon2 = gr.Accordion(open=False)
            with acordeon2: 
                gr.Button(value="Recargar Créditos ⚡", size='lg', link="https://splashmix.ink/buy", variant='primary')
 
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[input1, gender, personaje, usuario_firebase], 
            outputs=[result, lbl_console], 
            flagging_mode=globales.flag,
            js=fuego.js
            )        
    
    result.change(sulkuFront.actualizador_navbar, [usuario_firebase, result, lbl_console], acordeon2)
    btn_logout.click(welcome, usuario_firebase, btn_logout, js=aire.js)
    main.load(sulkuFront.precarga, usuario_firebase, [usuario_firebase, acordeon, acordeon2], js=fuego.js) if globales.acceso != "libre" else None
iniciar()