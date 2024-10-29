import gradio as gr
import subprocess
import os
import hug

#No está funcionando si es llamado por un cron, por eso por ahora no lo usaremos.
#hf_token = os.getenv('HF_TOKEN')
#print(hf_token)

hug = hug.hug
print(hug)

def iniciar():
    print("Lanzando bloque.")
    demo.launch(root_path="/mango", server_port=7860)

def greet(name):
    return f"Hola, hug  es {hug} - {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

iniciar()
