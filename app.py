import gradio as gr

def greet(name):
    return f"Hello, Hola, Tervetuloa, Cheers, Danke {name}."

try:
    demo = gr.Interface(fn=greet, inputs="text", outputs="text").launch(root_path="/gradio-demo")
except:
    raise gr.Error("ERROR 182")
    
#import gradio as gr
#import time

#def test(x):
#	time.sleep(4)
#	return x

#gr.Interface(test, "textbox", "textbox").queue().launch(root_path="/gradio-demo")
