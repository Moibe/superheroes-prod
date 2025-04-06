import inputs
import globales
import funciones
import sulkuFront
import gradio as gr
import firehead, fire, fuego 
import tools
mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang)

def welcome(result):

    print("Éste es el input resultado que estoy recibiendo: ")
    print(result) 
    return gr.Accordion(label="Moibe - 💶Creditos Disponibles: 182", open=False)

def iniciar():    
    app_path = globales.app_path
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

#fire provee las partes de javascript que se requieren para correr el chequeo de firebase.
with gr.Blocks(theme=globales.tema, head=firehead.head, js=fire.js, css="footer {visibility: hidden}") as main:
    
    usuario_firebase = gr.Textbox(visible=False) #Para almacenar el usuario de firebase 
    main.load(sulkuFront.precarga, usuario_firebase, usuario_firebase, js=fuego.js) if globales.acceso != "libre" else None

    with gr.Row():        
        with gr.Column(scale=5):
            with gr.Accordion(label="Moibe - 💶Creditos Disponibles: 0", open=False) as acordeon:
                with gr.Row():
                    gr.HTML()
                    gr.Button(scale=5, value="Recargar Créditos", size='sm', variant='secondary')
                    gr.Button(scale=5, value="Cerrar Sesión", size='sm', variant='stop')
        # with gr.Column(scale=5):
        #     gr.Label(label="Placeholder", visible=False) #Pon éste placeholder si quisieras la mitas de tamaño.
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[input1, gender, personaje, usuario_firebase], 
            outputs=[result, lbl_console], 
            flagging_mode=globales.flag
            )
        
    result.change(welcome, result, acordeon)
iniciar()