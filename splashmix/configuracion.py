import splashmix.static_databanks

#Creación indíca de que tendrá atributos el objeto.
creacion = "Superhero"    

#Indíca de q biblioteca se obtendrán los generales, por ahora: estilo.
general_databank = splashmix.static_databanks.general_data 

#Indíca de q biblioteca se obtendrán los rasgos particulares del objeto. 
selected_databank = splashmix.static_databanks.Superhero 

positions_path = "superheroes" #"girlsAllPositions" #superheroes
#Future, ve como usarás: prob_position = 0.1

#Para modificar el prompt usa: splashmix.prompter.prompteador