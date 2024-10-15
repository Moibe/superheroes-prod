import gradio as gr
import subprocess

def release_port(): 
    
    try:
        k = subprocess.check_output('lsof -i :7860 | kill xargs', shell=True, text=True)
        print("Processes on port 7860 killed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error killing processes:", e)

def iniciar():    
    print("Lanzando bloque.")
    demo.launch(root_path="/gradio-demo", server_port=7860)   

def greet(name):
    return f"Hello, Hola cambio con autoreload {name}."


with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

release_port()
iniciar()
