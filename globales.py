import gradio as gr
import tools

#aplicacion = "Moibe/image-blend"
aplicacion = "Kwai-Kolors/Kolors-Character-With-Flux"
work = "picswap"
app_path = "/mango"
server_port=7860
tema = tools.theme_selector()
#seto = "image-blend"
seto = "zhi"

print("El tema seleccionado es: ", tema)
print("Y su tipo es: ", type(tema))