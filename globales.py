import gradio as gr
import tools

aplicacion = "Moibe/image-blend"
work = "picswap"
app_path = "/mango"
server_port=7860
tema = tools.theme_selector

print("El tema seleccionado es: ", tema)
print("Y su tipo es: ", type(tema))



