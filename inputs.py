import gradio as gr

def inputs_selector(): 

    imagen = gr.Image(label="Source", type="filepath")

    print(" Imagen es del tipo: ", type(imagen))
    video = gr.Video(label="Destination")
    resultado_imagen = gr.Image(label="Result")

    input1 = imagen

    print("Input1 es del tipo: ", type(input1))

    return input1

inputs_selector()