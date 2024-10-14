import time
import gradio as gr
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def crearObserver():
    print("Inicio del programa...")
    observer = Observer()
    observer.schedule(MyHandler(), path='hola.py')
    observer.start()
    print("Observador iniciado, es este:", observer) 

    return observer


def iniciar():    
    
    print("Lanzando bloque.")
    demo.launch(root_path="/gradio-demo")

# Watch for changes in your Python file
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'hola.py':
            print("Creo que llegué aquí porque hubo un cambio1.")
            print("Y ésto es el observer:")
            print(observer)
            demo.close()
            crearObserver()
            print("Nuevo Observer creado...")
            time.sleep(7)            
            print("Demo closed...")
            print("Relanzando demo...")
            demo.launch(root_path="/gradio-demo")
            

def greet(name):
    print("Normal logging...")
    return f"Hello, Hola, Tervetuloa, Danke, Spasiva {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

try:
    observer = crearObserver() 
    iniciar()
    
    while True:
        print("Durmiendo 5 segundos...")
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
