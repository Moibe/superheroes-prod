def debita(path):

    print(f"El path final fue {path}, si es no-result, no debites y controla la info window.")
    print(f"El type de path es: ", type(path))  
    path_string = str(path)        
    print("Path_string = ", path_string)

    if "no-source-face" not in path_string:    
        return True
    else:
        return False  