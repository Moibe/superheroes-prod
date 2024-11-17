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
lbl_console = gr.Label(label="AI Terminal " + globales.version +  " messages", value="AI Engine ready...", container=True)
btn_buy = gr.Button("Get Credits", visible=False, size='lg')

#Customizable Inputs and Outputs
#Ésto era customizable así: input1, result, *resto = inputs.inputs_selector(globales.seto)
#Pero si será fijo para cada app arriba los inputs y outputs, ahora puedes mejor dejarlo fij de una.
input1, input2, result = inputs.inputs_selector(globales.seto)

#Por alguna razón, los elementos que pasan como *resto, pierden su type filepath y se vuelven numpy.
#Así es que la asignación del tipo la hago hasta acá.
#Quizá el problema de movidos es solo de labels, por lo tanto lo arreglaremos aquí.
# for elemento in resto:
#     elemento.type = "filepath"
#     elemento.label = "Labello"

with gr.Blocks(theme=globales.tema, css="footer {visibility: hidden}") as main:   
    #Cargado en Load: Función, input, output
    main.load(sulkuFront.display_tokens, None, html_credits) 
   
    with gr.Row():
        demo = gr.Interface(
            fn=funciones.perform,
            #inputs=[input1] + resto, #Éste es el que podría variar entre 1 o 2 inputs. #IMPORTANTE.
            inputs=[input1, input2], #Éste es el que podría variar entre 1 o 2 inputs.
            outputs=[result, lbl_console, html_credits, btn_buy], 
            flagging_mode="auto"
            )
iniciar()