def debita(path):
    #Future: Recuerda el problema de que si la destination no tiene un rostro detectable, no hay forma de que te avise.
    #...lo tendrás que corregir en el propio image-blend.
    path_string = str(path)        
    
    if "no-source-face" not in path_string:    
        return True
    else:
        return False  