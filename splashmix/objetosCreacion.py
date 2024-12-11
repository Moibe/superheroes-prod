import random
import importlib
import splashmix.configuracion
import splashmix.splash_tools as splash_tools

#DATA GENERAL: 
importable_general = "data." + splashmix.configuracion.databank_general 
databank_general = importlib.import_module(importable_general)

#DATA PARTICULAR (HG o SH):
importable_particular = "data." + splashmix.configuracion.selected_databank
databank_particular = importlib.import_module(importable_particular)

class Prompt:
    def __init__(self, style=None):              
        #Aquí pondrás cada atributo que contenga ese objeto general:
        self.style = style or random.choice(databank_general.lista_estilos)   

class Superhero(Prompt):
    def __init__(self,
                 subject=None, 
                 ):
        super().__init__()  # Call the parent class constructor
        #Random null para superheroe, porque podríamos quererlo genérico.
        self.subject = subject or splash_tools.randomNull(0.2, databank_particular.lista_subjects)
                        
class Hotgirl(Prompt):
    def __init__(self,
                 #Aquí pondrás cada atributo que contenga ese objeto general:
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
        
        self.subject = subject or splash_tools.randomNull(0.2, databank_particular.lista_subjects)
        self.adjective = adjective or splash_tools.randomNull(0.2, databank_particular.lista_adjective)
        self.type_girl = type_girl or splash_tools.randomNull(0.2, databank_particular.lista_type_girl)
        self.hair_style = hair_style or splash_tools.randomNull(0.2, databank_particular.lista_hair_style)
        self.boobs = boobs or splash_tools.randomNull(0.2, databank_particular.lista_boobs)
        self.wardrobe_top = wardrobe_top or splash_tools.randomNull(0.2, databank_particular.lista_wardrobe_top)
        self.wardrobe_accesories = wardrobe_accesories or splash_tools.randomNull(0.2, databank_particular.lista_wardrobe_accesories)
        self.wardrobe_bottom = wardrobe_bottom or splash_tools.randomNull(0.2, databank_particular.lista_wardrobe_bottom)
        self.wardrobe_shoes = wardrobe_shoes or splash_tools.randomNull(0.2, databank_particular.lista_wardrobe_shoes)
        self.situacion = situacion or splash_tools.randomNull(0.2, databank_particular.lista_situacion)
        self.place = place or splash_tools.randomNull(0.2, databank_particular.lista_place)
        self.complemento = complemento or splash_tools.randomNull(0.2, databank_particular.lista_complemento)