import gradio as gr
import tools

#MAIN
aplicacion = "Moibe/image-blend"
#aplicacion = "Kwai-Kolors/Kolors-Character-With-Flux"
seto = "image-blend"
#seto = "zhi"

work = "picswap"
app_path = "/boilerplate"
server_port=7860
tema = tools.theme_selector()
tema = gr.themes.Base()
print("Tema oficial: ", tema)