import gradio as gr
import tools

#MAIN
env = "dev"
aplicacion = "astroblend-dev"
api = "Moibe/image-blend"
#api = "Kwai-Kolors/Kolors-Character-With-Flux"
seto = "image-blend"
#seto = "zhi"

work = "picswap"
app_path = "/boilerplate"
server_port=7860
#tema = tools.theme_selector()
tema = gr.themes.Base()

sample_userfile = "gAAAAABmEZA4SLBC2YczouOrjIEi9WNCNGOIvyUcqBUnzxNsftXTdy54KaX9x8mAjFkABSI6FJrdZDQKk_5lpJOgJoMChxlniw=="
#Ojo, cuando el userfile termina con símbolo igual y supongo que también si empieza, causa problemas, la solución, ...
#... implementar más adelante desde ser agregar un caractér delimitador y despúes quitarlo, esto para evitar problemas...
#... con el símbolo =, ? y &. Dicho problema solo sucede cuando lo recibe como query params no como path params.
#... y todos los llamados son con path params.