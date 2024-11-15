import time
import inputs
import globales
import funciones
import sulkuFront
import autorizador
import gradio as gr

def iniciar():    
    app_path = globales.app_path
    main.launch(auth=autorizador.authenticate, root_path=app_path, server_port=globales.server_port)
    #Future: Si la app está dormida, no hay reacción de éste lado para avisar que está dormida.

#INTERFAZ

#Credit Related Elements
html_credits = gr.HTML(visible=True)
lbl_console = gr.Label(label="AI Terminal Messages", value="AI Engine ready...", container=True)
btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#Customizable Inputs and Outputs
#input1, result, *resto = inputs.inputs_selector(globales.seto)

#Por alguna razón, los elementos que pasan como *resto, pierden su type filepath y se vuelven numpy.
#Así es que la asignación del tipo la hago hasta acá.
# for elemento in resto:
#     elemento.type = "filepath"

input1 = gr.Image(label="Source", type="filepath")
input2 = gr.Textbox()
result = gr.Image(label="Result", type="filepath")

with gr.Blocks(theme=globales.tema, css="footer {visibility: hidden}") as main:   
    #Cargado en Load: Función, input, output
    main.load(sulkuFront.display_tokens, None, html_credits) 
   
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            inputs=[input1, input2], #Éste es el que podría variar entre 1 o 2 inputs.
            outputs=[result, lbl_console, html_credits, btn_buy], 
            flagging_mode='never'
            )
iniciar()