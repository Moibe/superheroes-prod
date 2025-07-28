import kraken
import tools
import globales
import fireWhale
import gradio as gr
from firebase_admin import firestore
mensajes, sulkuMessages = tools.get_mensajes(globales.mensajes_lang) #import modulo_correspondiente
import time

result_from_displayTokens = None 
result_from_initAPI = None    

def displayTokens(usuario):
    
    global result_from_displayTokens

    print("Entré a dipslay tokens, y ésto es usuario: ", usuario)

    #Obtengamos los datos hardcodeados del usuario mio, que no existe en las colecciones: 
    tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens')  
    
    novelty = fireWhale.obtenDato('usuarios', usuario, 'novelty' )
        
    if novelty == "new_user": 
        display = gr.Textbox(visible=False)
    else:
        tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens') 
        #tokens = sulkuPypi.getTokens(sulkuPypi.encripta(request.username).decode("utf-8"), globales.env)
        display = visualizar_creditos(tokens, usuario) 
    
    result_from_displayTokens = display

def precarga(uid):
    #gr.Info(title="¡Bienvenido!", message=mensajes.lbl_info_welcome, duration=None)

    print("Estoy en precarga y el valor de uid es: ", uid)
    if uid == None:
        #Aquí tenemos que hacer el redireccionamiento si no hay uid.
        mensaje = 'Necesitas loguearte al sistema.'
        mensaje2 = ''
        return uid, gr.Accordion(label=mensaje, open=True), gr.Button(value="Login 👋🏻"), gr.Accordion(label=mensaje2, open=False)
    
    else: #Si si hubo uid continuas el camino normal. 
        try: 
            #uid = 'IJNeNcHa5VPwTWDNcpMUyhGT5813' #Asumimos que ya lo traemos de auth y que aún no se guarda en firestore.
            
            email, displayName = fireWhale.obtenDatosUIDFirebase(uid)
            print(f"Email: {email}, displayName: {displayName}.")
            
            if email or displayName: #Si encontró a cualquiera de los dos significa que si existe en firebase auth.  
                #Camino 1: Si hubo un usuario.
                print("Camino 1") 
                tokens = fireWhale.obtenDato('usuarios', uid, 'tokens') #En firestore los usuarios estarán identificados por su uid de auth.
                if tokens is not None: #Significa que el usuario si tiene un registro previo en firebase.
                #La lógica de crear un usuario nuevo debería estar afuera, aquí.
                    print(f"Tokens: {tokens}.")
                    mensaje = f"🐙Usuario: {email} "
                    mensaje2 = f"💶Creditos Disponibles: {tokens}."
                else: #Si no se encontró significa que el usuario no existe en Firestore y deberíamos crear uno nuevo.
                    #Crear usuario nuevo en firestore, con 5 tokens y guarda su info de email y displayname.
                    #fireWhale.creaDato('usuarios', uid)
                    print("Camino 2: Usuario Nuevo:")
                    datos_perfil = {
                    'diplayName': displayName,
                    'email': email,
                    'tokens': 5,
                    'fecha_registro': firestore.SERVER_TIMESTAMP # Para un timestamp del servidor
                    }
                    fireWhale.creaDatoMultiple('usuarios', uid, datos_perfil)
                    mensaje = f"🐙Usuario: {email} "
                    mensaje2 = f"💶Creditos Disponibles: 5." #Analizar si está bien dejarlo fijo y todo funciona bien.
                    #Una vez creado, crea de una vez su usuario de Stripe.
                    site = "splashmix"
                    respuesta = kraken.crear_cliente_stripe(email, uid, site)
                    print("Respuesta de Kraken es: ")
                    print(respuesta)
                    fireWhale.editaDato('usuarios', uid, 'cus', respuesta['customer_id'])
                    print("cus agregado")
            else: #Si no existe en FIREBASE AUTH, es un usuario inválido. Future: ¿Debería regresarlo a login? 
                print("No hay email ni displayname?")
                mensaje = "Usuario inválido."
                mensaje2 = "Recarga la página si no puedes ver tus créditos." #Future,¿éste mensaje puede ser un link a login más que un texto?
        except Exception as e:
            f"Excepción: {e}"
            
        return uid, gr.Accordion(label=mensaje, open=False), gr.Accordion(label=mensaje2, open=False)  

def visualizar_creditos(nuevos_creditos, usuario):

    html_credits = f"""
    <div>
    <div style="text-align: left;">👤<b>{mensajes.lbl_username}: </b> {usuario}</div><div style="text-align: right;">💶<b>{mensajes.lbl_credits}: </b> {nuevos_creditos}</div>
    </div>
                    """    
     
    return html_credits

#Controla lo que se depliega en el frontend y que tiene que ver con llamados a Sulku.
def noCredit():
    info_window = sulkuMessages.out_of_credits
    path = 'images/no-credits.png'
    return path, info_window 

def aError(excepcion):
    print("La excepción es:", excepcion)
    info_window = manejadorExcepciones(excepcion)
    path = 'images/error.png'      
    return path, info_window

def manejadorExcepciones(excepcion):
    #El parámetro que recibe es el texto despliega ante determinada excepción:
    if excepcion == "PAUSED": 
        info_window = sulkuMessages.PAUSED
    elif excepcion == "RUNTIME_ERROR":
        info_window = sulkuMessages.RUNTIME_ERROR
    elif excepcion == "STARTING":
        info_window = sulkuMessages.STARTING
    elif excepcion == "HANDSHAKE_ERROR":
        info_window = sulkuMessages.HANDSHAKE_ERROR
    elif excepcion == "GENERAL":
        info_window = sulkuMessages.GENERAL
    elif excepcion == "NO_FACE":
        info_window = sulkuMessages.NO_FACE
    elif excepcion == "NO_FILE":
        info_window = sulkuMessages.NO_FILE
    elif excepcion == "NO_POSITION": #Solo aplíca para Splashmix.
        info_window = sulkuMessages.NO_POSITION
    elif "quota" in excepcion: #Caso especial porque el texto cambiará citando la cuota.
        info_window = excepcion
    else:
        info_window = sulkuMessages.ELSE

    return info_window

def evaluaResultadoUsuario(resultado, personaje): 

    if "image.webp" in resultado:
        #Si es imagen, debitarás.
        resultado = tools.renombra_imagen(personaje, resultado)
        #accion = "no-debitar" if globales.acceso == "libre" else "debita"
        info_window = sulkuMessages.result_ok
    else: #CUANDO NO TRAE IMAGEN EL ERROR QUE PODRÍA TRAER ES NO_FACE O GENERAL (y ambos significarían que no detecto rostro).
        #Si no es imagen es un texto que nos dice algo.
        resultado, info_window = aError(excepcion = resultado)
        return resultado, info_window         
           
    return resultado, info_window
    
def presentacionFinal(usuario, accion):        
    
    if accion == "debita":        
        tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens') #obtienes
        tokens = tokens - globales.costo_work #debitas
        fireWhale.editaDato('usuarios', usuario, 'tokens', tokens) #editas
        print(f"Después de debitar tienes {tokens} tokens.")
        info_window = sulkuMessages.result_ok
    elif accion == "no-debitar": #Aquí llega si está en modo libre.
        info_window = sulkuMessages.result_ok
        tokens = "Free"        
    else: 
        info_window = "No face in source path detected."
        #tokens = sulkuPypi.getTokens(capsule, globales.env)
        tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens')
    
    html_credits = visualizar_creditos(tokens, usuario)       
    
    return html_credits, info_window

def actualizador_navbar(usuario, result, info_window):
    print("Estoy en actualizador de navbar...")

    #Dependiendo del resultado obtenido deberé debitar o no:     
    #Cuando no hay imagen (Error directo de mass): error.png 

    if "jpg" in result: #Cuando la imagen es correcta. El resultado es un archivo .jpg
        #Debita uno de la cuota de ese usuario y despliegalo.
        tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens') #obtienes
        print("Estos son los tokens que tiene actualmente el usuario:", tokens)
        tokens = tokens - globales.costo_work #debitas
        fireWhale.editaDato('usuarios', usuario, 'tokens', tokens) #editas
        print(f"Después de debitar tienes {tokens} tokens.")
    else: 
        #Lo demás debería ser un error.
        print("Resultado incorrecto e incobrable...")
        #Future, también podrías no hacer la ida a firebase y obtenerlo de valor previo.
        tokens = fireWhale.obtenDato('usuarios', usuario, 'tokens') #obtienes
        print("Estos son los tokens que tiene actualmente el usuario:", tokens)
        #Por ahora no debites.
    return gr.Accordion(label=f"Moibe - 💶Creditos Disponibles: {tokens}", open=False)