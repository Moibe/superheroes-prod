import gradio_client
import hug

def consulta(): 

    abrazo = hug.hug
    print(abrazo)

    client = gradio_client.Client("Moibe/basico", hf_token=abrazo)

    print("Ésto es el cliente obtenido: ")
    print(client)

    return client