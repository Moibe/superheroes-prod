import gradio as gr
import tools

#MAIN
aplicacion = "Moibe/image-blend"
#aplicacion = "Kwai-Kolors/Kolors-Character-With-Flux"
#aplicacion = "Kwai-Kolors/Kolors-Portrait-with-Flux"
seto = "image-blend"
#seto = "zhi"

work = "picswap"
app_path = "/boilerplate"
server_port=7861
tema = tools.theme_selector()

print("El tema seleccionado es: ", tema)
print("Y su tipo es: ", type(tema))