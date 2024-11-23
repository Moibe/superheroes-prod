import random
import splash_tools
import importlib
import configuracion.globales as globales
import data.data as data, data.data_girls as data_girls, data.data_heroes as data_heroes #puede ya no necesitarse.

#data general: 
importable_general = "data." + globales.databank_general 
#print("IMPORTABLE GENERAL ES: ", importable_general)
modulo_general = importlib.import_module(importable_general)

importable = "data." + globales.selected_databank
#importable = "data." + globales.databank_girls 
#print("IMPORTABLE ES: ", importable)
#importable = "data." + globales.databank_girls
modulo = importlib.import_module(importable)

class Prompt:
    #Future, que el databank se defina arriba para todos.
    def __init__(self, style=None):              
        databank_general = modulo_general
        self.style = style or random.choice(databank_general.lista_estilos)   

#Aplica la función randomNull para aquellos valores de una lista en donde deseas que también exista la posibilidad...
#...de que no regrese nada.

class Superhero(Prompt):
    def __init__(self,
                 subject=None, 
                 ):
        super().__init__()  # Call the parent class constructor
        #Se especifica cuál es su databank:
        #IMPORTANTE: Databank son las variables que rellenan los atributos de cada objeto, al gusto de un cliente en específico.
        #Por ejemplo, el objeto es heroes, pero el cliente en particular es RevGenLabs, que tiene su propio databank ...
        #...crafted a su gusto.
        databank = modulo
        #Random null es una función que regresa al sujeto pero también puede no regresar nada, añadir q probabilidades...
        #de que eso suceda se desean.
        self.subject = subject or splash_tools.randomNull(0.2, databank.lista_subjects)
                        
class Hotgirl(Prompt):
    def __init__(self,
                 style=None,
                 subject=None,
                 adjective=None,
                 type_girl=None,
                 hair_style=None,
                 boobs=None,
                 wardrobe_top=None,
                 wardrobe_accesories=None,
                 wardrobe_bottom=None,
                 wardrobe_shoes=None,
                 situacion=None,
                 place=None,
                 complemento=None,
                 ):
        super().__init__(style)  # Call the parent class constructor

        #Se especifica cuál es su databank:
        databank = modulo
        
        self.subject = subject or random.choice(databank.lista_subjects)
        self.adjective = adjective or random.choice(databank.lista_adjective)
        self.type_girl = type_girl or random.choice(databank.lista_type_girl)
        self.hair_style = hair_style or random.choice(databank.lista_hair_style)
        self.boobs = boobs or random.choice(databank.lista_boobs)
        self.wardrobe_top = wardrobe_top or random.choice(databank.lista_wardrobe_top)
        self.wardrobe_accesories = wardrobe_accesories or random.choice(databank.lista_wardrobe_accesories)
        self.wardrobe_bottom = wardrobe_bottom or random.choice(databank.lista_wardrobe_bottom)
        self.wardrobe_shoes = wardrobe_shoes or random.choice(databank.lista_wardrobe_shoes)
        self.situacion = situacion or random.choice(databank.lista_situacion)
        self.place = place or random.choice(databank.lista_place)
        self.complemento = complemento or random.choice(databank.lista_complemento)