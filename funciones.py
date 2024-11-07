import time
import bridges
import globales
import gradio_client

abrazo = bridges.hug

def mass(input1, input2): 

    imagenSource = gradio_client.handle_file(input1) 
    imagenDestiny = gradio_client.handle_file(input2)       

    client = gradio_client.Client(globales.aplicacion, hf_token=abrazo)
    result = client.predict(imagenSource, imagenDestiny, api_name="/predict")

    return result