import gradio as gr
import subprocess
import os

# Para obtener el valor de una variable de entorno:
mi_variable = os.getenv('NOMBRE_DE_LA_VARIABLE')

api_key = os.getenv('API_KEY')
print(api_key)

def iniciar():    
    print("Lanzando bloque.")
    demo.launch(root_path="/gradio-demo", server_port=7860)   

def greet(name):
    return f"3rd Print: {api_key} - {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

iniciar()
