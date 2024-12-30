import splashmix.static_databanks

#Indíca de q biblioteca se obtendrán los generales, por ahora: estilo.
general_databank = splashmix.static_databanks.general_data 

# Definimos una variable para almacenar el nombre del diccionario
nombre_diccionario = "datos_superheroe"  # Puedes cambiar esto a "datos_superheroine" o cualquier otro nombre

datos_superheroe = {
    "creacion": "Superhero",
    "selected_databank": splashmix.static_databanks.Superhero,
    "positions_path": "superheroes"
}

datos_superheroine = {
    "creacion": "Superheroine",
    "selected_databank": splashmix.static_databanks.Superheroine,
    "positions_path": "girlPositions"
}

#Para modificar el prompt usa: splashmix.prompter.prompteador


# creacion = "Superhero"   
# selected_databank = splashmix.static_databanks.Superhero 
# positions_path = "superheroes"