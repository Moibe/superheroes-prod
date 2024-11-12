import sulkuFront
import autorizador
import time
import funciones
import globales
import gradio as gr

def iniciar():    
    app_path = globales.app_path
    main.launch(auth=autorizador.authenticate, root_path=app_path, server_port=globales.server_port)
    #Future: Si la app está dormida, no hay reacción de éste lado para avisar que está dormida.

#INTERFAZ

#Credit Related Elements
html_credits = gr.HTML(visible=True)
lbl_console = gr.Label(label="AI Terminal Messages", value="AI Engine ready...", container=True)
btn_buy = gr.Button("Get Credits", visible=True, size='lg')

#Customizable Inputs and Outputs
source_image = gr.Image(label="Source", type="filepath")
destination_image = gr.Image(label="Destination", type="filepath")
result_image = gr.Image(label="Blend Result")

with gr.Blocks(theme=globales.tema, css="footer {visibility: True}") as main:   
    #Cargado en Load: Función, input, output
    main.load(sulkuFront.display_tokens, None, html_credits) 
   
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[source_image, destination_image], 
            outputs=[result_image, lbl_console, html_credits, btn_buy], 
            allow_flagging='never'
            )     

iniciar()