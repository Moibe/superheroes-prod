import gradio as gr
import funciones




def greet(name):
    #Conexión con API principal: 
    result = funciones.consulta(name)
    return f"Hola, el resultado es {result} - {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")


