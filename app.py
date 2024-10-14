import gradio as gr

def iniciar():    
    print("Lanzando bloque.")
    demo.launch(root_path="/gradio-demo")   

def greet(name):
    return f"Hello, Hola cambio con reload {name}."


with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

iniciar()
