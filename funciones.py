import gradio_client
import bridges

abrazo = bridges.hug
print(abrazo)

def consulta(texto):     

    client = gradio_client.Client("Moibe/basico", hf_token=abrazo)

    print("Ésto es el cliente obtenido: ")
    print(client)

    result = client.predict(texto, api_name="/predict")

    return result

def mass(input1, input2): 

    imagenSource = gradio_client.handle_file(input1) 
    imagenDestiny = gradio_client.handle_file(input2)       

    client = gradio_client.Client("Moibe/image-blend", hf_token=abrazo)
    result = client.predict(imagenSource, imagenDestiny, api_name="/predict")

    print("Ésto es el cliente obtenido: ")
    print(client)

    return result