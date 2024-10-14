import time
import gradio as gr
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Watch for changes in your Python file
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'app.py':
            print("Creo que llegué aquí porque hubo un cambio.")
            demo.close()
            demo.launch(root_path="/gradio-demo")

def greet(name):
    print("Normal logging...")
    return f"Hello, Hola {name}."

print("Inicio del programa...")
observer = Observer()
observer.schedule(MyHandler(), path='app.py')
observer.start()
print("Observador iniciado")

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

print("Lanzando bloque.")
demo.launch(root_path="/gradio-demo")


try:
    while True:
        print("Durmiendo 5 segundos...")
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
