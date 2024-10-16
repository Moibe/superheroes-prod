import gradio as gr
import subprocess

def iniciar():    
    print("Lanzando bloque.")
    demo.launch(root_path="/gradio-demo", server_port=7860)   

def greet(name):
    return f"Idempotencia: {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

iniciar()
