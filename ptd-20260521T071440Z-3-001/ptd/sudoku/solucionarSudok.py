import requests
def falta(llista):
    
    r= []
    for i in range (1,9):
        try:
            llista.index(i)
            print(i, "present")
            
        except ValueError:
            print(i, "no present")
            r.append(i)
            print(r)
    return r



#.pop -> borrar

fila= [0,1,4,7,8]
falta(fila)