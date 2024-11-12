def debita(path):

    #Future: Recuerda el problema de que si la destination no tiene un rostro detectable, no hay forma de que te avise.
    #...probablemente lo tendrás que corregir en el propio image-blend.
    print(f"El path final fue {path}.")
    print(f"El type de path es: ", type(path))  
    path_string = str(path)        
    print("Path_string = ", path_string)

    if "no-source-face" not in path_string:    
        return True
    else:
        return False  