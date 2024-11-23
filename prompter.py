from objetosCreacion import Hotgirl, Superhero
import time
import configuracion.splashmix

def obten(dataframe, indice, atributo):        
    valor = dataframe.loc[indice[0], atributo]  
    return valor

def obtenAtributosObjeto(sample_objeto):     

    atributos = []

    for nombre_atributo in dir(sample_objeto):
        if not nombre_atributo.startswith("__"):
            atributos.append(nombre_atributo)

    return atributos


def creaContenedorTemplate(dataframe, indice, objeto):
    
    #Prompt es la frase que ordena a los atributos que ya tenemos.
    if objeto == "Superhero":
        sample_objeto = Superhero()
    else:
        sample_objeto = Hotgirl()
    
    #Obtiene los atributos del tipo de objeto, por ejemplo style y heroe.
    atributos = obtenAtributosObjeto(sample_objeto)

    contenedor = {}

    for atributo in atributos:
        
        contenedor[atributo] = obten(dataframe, indice, atributo) if isinstance(obten(dataframe, indice, atributo), str) else ""
 
        
    #Al final agrega el shot porque siempre lo traerá.
    contenedor['shot'] = obten(dataframe, indice, 'Shot')
     
    return contenedor

def creaPrompt(contenedor, creacion):

    #FUTURE: Detectar atributos dinámicamente.

    if creacion == "Superhero":              

        style = contenedor['style'] #if isinstance(contenedor.get('style'), str) else ""
        subject = contenedor['subject'] #if isinstance(contenedor.get('style'), str) else ""  
    
    
        #PROMPT PARA HEROE
        prompt = f"A {style} of a superhero like {subject} " #agregar otros atributos random aquí posteriormente.
   
    
    else:
            
        #Importante El if instance es porque si viene como float nan, lo cambio a texto que sea vacío.
        #Porque si no me parece que deja la palabra nan o lo manifiesta como float, tendríamos que probar.
        style = contenedor['style'] #if isinstance(contenedor.get('style'), str) else ""
        adjective = contenedor['adjective'] #if isinstance(contenedor.get('adjective'), str) else ""
        boobs = contenedor['boobs'] #if isinstance(contenedor.get('style'), str) else ""
        complemento = contenedor['complemento'] #if isinstance(contenedor.get('style'), str) else ""
        hair_style = contenedor['hair_style'] #if isinstance(contenedor.get('style'), str) else ""
        place = contenedor['place'] #if isinstance(contenedor.get('place'), str) else ""
        situacion = contenedor['situacion'] #if isinstance(contenedor.get('style'), str) else ""
        subject = contenedor['subject'] #if isinstance(contenedor.get('style'), str) else ""
        type_girl = contenedor['type_girl'] #if isinstance(contenedor.get('style'), str) else ""
        wardrobe_top = contenedor['wardrobe_top'] #if isinstance(contenedor.get('style'), str) else ""
        wardrobe_accesories = contenedor['wardrobe_accesories'] #if isinstance(contenedor.get('style'), str) else ""
        wardrobe_bottom = contenedor['wardrobe_bottom'] #if isinstance(contenedor.get('style'), str) else ""
        wardrobe_shoes = contenedor['wardrobe_shoes'] #if isinstance(contenedor.get('style'), str) else ""
        
        prompt = f"""A {style} of a {adjective} {type_girl} {subject} with {boobs} and {hair_style} wearing {wardrobe_top}, 
                {wardrobe_accesories}, {wardrobe_bottom}, {wardrobe_shoes}, {situacion} at {place} {complemento}"""   

    return prompt

def prompteador(objeto):

    print("Entré al prompteador...")
 
    if  configuracion.splashmix.creacion == "Superhero":
 
        #PROMPT PARA HEROE
        prompt = f"A {objeto.style} of a superhero like {objeto.subject} " #agregar otros atributos random aquí posteriormente.
        print("Éste es el prompt:")
        print(prompt)
    
    else:
        
        #Importante El if instance es porque si viene como float nan, lo cambio a texto que sea vacío.
        #Porque si no me parece que deja la palabra nan o lo manifiesta como float, tendríamos que probar.

        # style = contenedor['style'] #if isinstance(contenedor.get('style'), str) else ""
        # adjective = contenedor['adjective'] #if isinstance(contenedor.get('adjective'), str) else ""
        # boobs = contenedor['boobs'] #if isinstance(contenedor.get('style'), str) else ""
        # complemento = contenedor['complemento'] #if isinstance(contenedor.get('style'), str) else ""
        # hair_style = contenedor['hair_style'] #if isinstance(contenedor.get('style'), str) else ""
        # place = contenedor['place'] #if isinstance(contenedor.get('place'), str) else ""
        # situacion = contenedor['situacion'] #if isinstance(contenedor.get('style'), str) else ""
        # subject = contenedor['subject'] #if isinstance(contenedor.get('style'), str) else ""
        # type_girl = contenedor['type_girl'] #if isinstance(contenedor.get('style'), str) else ""
        # wardrobe_top = contenedor['wardrobe_top'] #if isinstance(contenedor.get('style'), str) else ""
        # wardrobe_accesories = contenedor['wardrobe_accesories'] #if isinstance(contenedor.get('style'), str) else ""
        # wardrobe_bottom = contenedor['wardrobe_bottom'] #if isinstance(contenedor.get('style'), str) else ""
        # wardrobe_shoes = contenedor['wardrobe_shoes'] #if isinstance(contenedor.get('style'), str) else ""
        
        prompt = f"""A {objeto.style} of a {objeto.adjective} {objeto.type_girl} {objeto.subject} with {objeto.boobs} and {objeto.hair_style} wearing {objeto.wardrobe_top}, 
                {objeto.wardrobe_accesories}, {objeto.wardrobe_bottom}, {objeto.wardrobe_shoes}, {objeto.situacion} at {objeto.place} {objeto.complemento}"""   
        print("Éste es el prompt:")
        print(prompt)
        
    return prompt