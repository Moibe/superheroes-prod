import sulkuPypi
import gradio as gr
import time

def debita(usuario):
     #Si el path NO tiene no-result, todo funcionó bien, por lo tanto debita.
        print("182: Acabo de entrar a debita...")
        print(usuario)
        time.sleep(18)
        print("Se obtuvo un resultado, debitaremos.")
        #Y finalmente debita los tokens.
        #IMPORTANTE: Tienes que reconstruir capsule ahora que ya se obtiene del request, sino, capsule sera un State para el uso...
        #...de todos y es ahí donde radica el problema: 
        capsule = sulkuPypi.encripta(usuario).decode("utf-8") #decode es para quitarle el 'b
        tokens = sulkuPypi.debitTokens(capsule, "picswap")
        html_credits = actualizar_creditos(tokens, usuario)
        print(f"html credits quedó como : {html_credits} y es del tipo: {type(html_credits)}")
        info_window = "Image ready!"

        return info_window

def noDebita():
     pass

def display_tokens(request: gr.Request):

    print("182: Hola estoy en display_tokens y gr.Request.username es: ")
    print(request.username)
    time.sleep(18)

    #Para desplegar o no desplegar, necesitamos saber si el usuario es new user.
    flag = sulkuPypi.getFlag(sulkuPypi.encripta(request.username).decode("utf-8"))
    print("La flag obtenida es: ", flag)
    #FUTURE quizá das doble vuelta decodificando porque haya lo vuelves a encodear, prueba enviando sin decode...
    #...llegaría codificado a encripta y prueba allá no encode.
    tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"))
    display = actualizar_creditos(tokens, request.username)
    
    return display

def actualizar_creditos(nuevos_creditos, usuario):

     html_credits = f"""
     <div>
     <div style="text-align: left;">👤<b>Username: </b> {usuario}</div><div style="text-align: right;">💶<b>Credits Available: </b> {nuevos_creditos}</div>
     </div>
                       """
     
     return html_credits