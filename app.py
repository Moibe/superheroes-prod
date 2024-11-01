import gradio as gr
import funciones
import hug

def iniciar():
    print("Lanzando bloque.")
    cliente = funciones.consulta()
    print("Cliente: ", cliente)
    demo.launch(root_path="/mango", server_port=7860)

def greet(name):
    return f"Hola, hug  es {hug} - {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

iniciar()
