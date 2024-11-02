import gradio as gr
import sulkuPypi
from funciones import mass
import tools
import auth

#Funciones

#Función principal
def perform(input1, input2, request: gr.Request):
    
    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8")) #Todo en una línea.
        
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

    if "no-source-face" not in path_string:
        #Si el path NO tiene no-result, todo funcionó bien, por lo tanto debita.
        print("Se obtuvo un resultado, debitaremos.")
        #Y finalmente debita los tokens.
        #IMPORTANTE: Tienes que reconstruir capsule ahora que ya se obtiene del request, sino, capsule sera un State para el uso...
        #...de todos y es ahí donde radica el problema: 
        capsule = sulkuPypi.encripta(request.username).decode("utf-8") #decode es para quitarle el 'b
        tokens = sulkuPypi.debitTokens(capsule, "picswap")
        html_credits = tools.actualizar_creditos(tokens, request.username)
        print(f"html credits quedó como : {html_credits} y es del tipo: {type(html_credits)}")
        info_window = "Image ready!"
        
    else:
        print("No se detectó un rostro...")
        info_window = "No face in source path detected."
        html_credits = tools.actualizar_creditos(tokens, request.username)        
        #No se hizo un proceso, por lo tanto no debitaremos.
        #En el futuro, como regla de negocio, podría cambiar y que si debitemos.  
    
    return path, info_window, html_credits, btn_buy

def display_tokens(request: gr.Request):

    #Para desplegar o no desplegar, necesitamos saber si el usuario es new user.
    flag = sulkuPypi.getFlag(sulkuPypi.encripta(request.username).decode("utf-8"))
    print("La flag obtenida es: ", flag)
    #FUTURE quizá das doble vuelta decodificando porque haya lo vuelves a encodear, prueba enviando sin decode...
    #...llegaría codificado a encripta y prueba allá no encode.
    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"))
    display = tools.actualizar_creditos(tokens, request.username)
    
    return display

#Inputs
source_image = gr.Image(label="Source")
destination_image = gr.Image(label="Destination")

#Outputs
creditos = None 
result_image = gr.Image(label="Blend Result")
txt_credits = gr.Textbox(label="Credits Available", value="", interactive=False)
html_credits = gr.HTML()
lbl_console = gr.Label(label="AI Terminal Messages", value="AI Engine ready...", container=True)
btn_buy = gr.Button("Buy More", visible=False, size='lg')

with gr.Blocks(theme=gr.themes.Base(), css="footer {visibility: True}") as main:
   
    #Cargado en Load, Función, input, output
    main.load(display_tokens, None, html_credits) 
   
    with gr.Row():
        demo = gr.Interface(
            fn=perform,
            inputs=[source_image, destination_image], 
            outputs=[result_image, lbl_console, html_credits, btn_buy], 
            allow_flagging='never'
            )        
        
main.launch(auth=auth.authenticate)