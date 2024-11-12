import time 
import gradio as gr

def inputs_selector(set):

    # Diccionario para mapear los sets a sus respectivas configuraciones
    configuraciones = {
        "image-blend": {
            "input1": gr.Image(label="Source", type="filepath"),
            "input2": gr.Image(label="Destination", type="filepath"),
            "result": gr.Image(label="Result"),
        },
        "video-blend": {
            "input1": gr.Image(label="Source", type="filepath"),
            "input2": gr.Video(),
            "result": gr.Video() 
        },
        "sampler": {
            "input1": gr.Audio(),
            "input2": gr.Audio(),
            "result": gr.Audio() 
        },
        "splashmix": {
            "input1": gr.Image(label="Source", type="filepath"),
            "result": gr.Image(label="Source", type="filepath"),
        },
    }

    # Obtener la configuración según el valor de 'set'
    config = configuraciones.get(set)
    print("El tamaño del set config es:", len(config))

    # Si la configuración existe, usarla
    if config:
        if len(config) == 2:
            input1 = config["input1"]
            result = config["result"]
            return input1, result
        elif len(config) == 3:
            input1 = config["input1"]
            input2 = config["input2"]
            result = config["result"]
            return input1, input2, result
    else:
        print("Set no válido")