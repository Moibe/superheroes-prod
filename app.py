import time
import gradio as gr
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def slow_echo(message, history):
    for i in range(len(message)):
        time.sleep(0.05)
        yield "You typed: " + message[: i + 1]

def greet(name):
    print("Normal logging...")
    return f"Hello, Hola, Tervetuloa, Danke, Spasiva {name}."

with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output, api_name="greet")

demo.launch(root_path="/gradio-demo")

print("Demo lanzado, llegamos a éste punto??")

# Watch for changes in your Python file
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == 'app.py':
            print("Creo que llegué aquí porque hubo un cambio.")
            demo.close()
            demo.launch()

observer = Observer()
observer.schedule(MyHandler(), path='app.py')
observer.start()

try:
    while True:
        print("Durmiendo 5 segundos...")
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()
observer.join()
