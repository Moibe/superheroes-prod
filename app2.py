import gradio as gr
import sulkuPypi
from funciones import mass
import SulkuFront
import autorizador
import time

def iniciar():    
    main.launch(auth=autorizador.authenticate, root_path="/mango", server_port=7860)

#Función principal
def perform(input1, input2, request: gr.Request):
            
    #Después autoriza.
    #Si está autorizada puede ejecutar la tarea, ésta lógica si está a cargo aquí, por parte de la app y su desarrollador, no de Sulku.
    autorizacion = sulkuPypi.authorize(gr.State.tokens, 'picswap')
    print("La autorización es: ", autorizacion)
      
    if autorizacion is True:    
        path = mass(input1,input2)
    else:
        info_window = "Out of credits..."
        path = 'no-credits.png'
        return path, info_window, html_credits, btn_buy

    print(f"El path final fue {path}, si es no-result, no debites y controla la info window.")
    print(f"El type de path es: ", type(path))  
    print("Convirtiendo path a string...")
    path_string = str(path)    
    
    print("Path_string = ", path_string)

    #Condicionales Inherentes a ésta app, ¿deberían ir aquí? 
    if "no-source-face" not in path_string:
        
        info_window = SulkuFront.debita(request.username)
        
    else:
        print("No se detectó un rostro...")
        info_window = "No face in source path detected."
        html_credits = SulkuFront.actualizar_creditos(gr.State.tokens, request.username)        
        #No se hizo un proceso, por lo tanto no debitaremos.
        #En el futuro, como regla de negocio, podría cambiar y que si debitemos.  
    
    return path, info_window, html_credits, btn_buy, creditos


#Inputs
source_image = gr.Image(label="Source", type="filepath")
destination_image = gr.Image(label="Destination", type="filepath")

#Outputs
creditos = None
result_image = gr.Image(label="Blend Result")
txt_credits = gr.Textbox(label="Credits Available", value="", interactive=False)
html_credits = gr.HTML()
lbl_console = gr.Label(label="AI Terminal Messages", value="AI Engine ready...", container=True)
btn_buy = gr.Button("Buy More", visible=False, size='lg')

with gr.Blocks(theme=gr.themes.Base(), css="footer {visibility: True}") as main:
   
    #Cargado en Load, Función, input, output
    main.load(SulkuFront.display_tokens, None, html_credits) 
   
    with gr.Row():
        demo = gr.Interface(
            fn=perform,
            inputs=[source_image, destination_image], 
            outputs=[result_image, lbl_console, html_credits, btn_buy], 
            allow_flagging='never'
            )     

iniciar()