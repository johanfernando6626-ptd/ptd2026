def comprovaGrup(grup):
    tots = [1,2,3,4,5,6,7,8,9]
    
    for i in range(len(grup)):
        print ("El valor de tots és", grup[i])
        
        if (grup[i] in tots):
            tots.remove(grup[i])
        print("llista grup", grup)
        print("llista tots", tots)
        
        

    return False
fila = [1,2,4,4,2,2,7,8,9]
comprovaGrup(fila)
