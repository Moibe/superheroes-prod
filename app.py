import gradio as gr

def greet(name):
    return f"Hello, Hola, Tervetuloa, Cheers, Danke {name}."

gr.Interface(fn=greet, inputs="text", outputs="text").launch(demo_name="demo", root_path="/gradio-demo")


#import gradio as gr
#import time

#def test(x):
#	time.sleep(4)
#	return x

#gr.Interface(test, "textbox", "textbox").queue().launch(root_path="/gradio-demo")
