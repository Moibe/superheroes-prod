import gradio_client
import hug

def consulta(texto): 

    abrazo = hug.hug
    print(abrazo)

    client = gradio_client.Client("Moibe/basico", hf_token=abrazo)

    print("Ésto es el cliente obtenido: ")
    print(client)

    result = client.predict(texto, api_name="/predict")

    return result