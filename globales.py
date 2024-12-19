import gradio as gr

#MAIN
version = "5.15.18"
env = "dev"
aplicacion = "superheroes-dev" #como se llama en tu repo y tu dominio.

#api = "Moibe/splashmix"
api_zero = "Moibe/InstantID2" #Risky but leave @ 25.
api_cost = "Moibe/InstantID2-B" #Corriendo en Zero, 22 segundos. Quota limitada.
same_api = False #Hay diferencia en las apis por eso si se debe correr proceso de selección.
#api = "charlieguo610/InstantID" #Corriendo en A10G, 22 segundos. Libre!! 
#api = "InstantX/InstantID" #Como es externa pide 60s.

process_cost = 25

seto = "splashmix"
work = "picswap"
app_path = "/superheroes-dev"
server_port=7880
tema = gr.themes.Default()
flag = "auto"