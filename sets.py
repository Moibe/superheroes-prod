import gradio as gr

# Diccionario para mapear los sets a sus respectivas configuraciones
configuraciones = {
    "image-blend": {
        "input1": gr.Image(label="Arriba", type="filepath"),
        "input2": gr.Image(label="Abajo", type="filepath"),
        "result": gr.Image(label="Derecha"),
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
    "txt2image": {
        "input1": gr.Textbox(),
        "result": gr.Image(label="Source", type="filepath"),
    },
    "txt2video": {
        "input1": gr.Textbox(),
        "result": gr.Video(),
    },
}