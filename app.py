import gradio as gr
import sulkuPypi
import SulkuFront
import autorizador
import time
import debit_rules
from funciones import mass

def iniciar():    
    main.launch(auth=autorizador.authenticate, root_path="/mango", server_port=7860)

#Función principal
def perform(input1, input2, request: gr.Request):            
    
    #1: Reglas sobre autorización si se tiene el crédito suficiente.
    autorizacion = sulkuPypi.authorize(gr.State.tokens, 'picswap')
    if autorizacion is True:
        #IMPORTANTE: EJECUCIÓN DE LA APP EXTERNA: mass siempre será la aplicación externa que consultamos via API.   
        resultado = mass(input1,input2)
    else:
        info_window, resultado = SulkuFront.noCredit()
        return resultado, info_window, html_credits, btn_buy
    
    #**SE EJECUTA EL LLAMADO Y OFRECE UN RESULTADO.**
    
    #2: ¿El resultado es debitable?
    if debit_rules.debita(resultado) == True:
        html_credits, info_window = SulkuFront.presentacionFinal(request.username, "debita")
    else:
        html_credits, info_window = SulkuFront.presentacionFinal(request.username, "no debita") 
            
    #Lo que se le regresa oficialmente al entorno.
    return resultado, info_window, html_credits, btn_buy

#INTERFAZ

#Inputs
source_image = gr.Image(label="Source", type="filepath")
destination_image = gr.Image(label="Destination", type="filepath")

#Outputs
result_image = gr.Image(label="Blend Result")
txt_credits = gr.Textbox(label="Credits Available", value="", interactive=False)
html_credits = gr.HTML()
lbl_console = gr.Label(label="AI Terminal Messages", value="AI Engine ready...", container=True)
btn_buy = gr.Button("Buy More", visible=False, size='lg')

with gr.Blocks(theme=gr.themes.Base(), css="footer {visibility: True}") as main:
   
    #Cargado en Load: Función, input, output
    main.load(SulkuFront.display_tokens, None, html_credits) 
   
    with gr.Row():
        demo = gr.Interface(
            fn=perform,
            inputs=[source_image, destination_image], 
            outputs=[result_image, lbl_console, html_credits, btn_buy], 
            allow_flagging='never'
            )     

iniciar()