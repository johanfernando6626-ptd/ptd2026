def quifalta(llista):
    #funció que ens retorna els nombres que falten d'una llista de 1 a 9

    r = []

    for i in range(1,10):
        try:
            llista.index(i)
            print(i, "present")
        except ValueError:
            print(i, "no preset")
            r.append(i)
            print(r)
    return r

def troba(e1,e2,e3):
    #funció que ens retorna els nombres que falten d'una llista de 1 a 9

    t = []
    
    for j in range (1,10):
        if (j in e1) and (j in e2) and (j in e3) : # && (j in e2) or (j in e3):#j==1[0]==e2[1]==e3[1])
            t.append(j)
            print("afegit",j)
    return t

for i in range (1,10):
    for j in range (1,10):
        if (sudoku[i][j]==0):
            fila, columna, grup
            falta = miraquifalta (fila, columna, grup)
    for n in range(1,10):
        fila.append(sudoku [i][n])  
    for n in range(1,10):
        columna.append(sudoku [i][n])


#print("falten els elements: ", elementsQueFalten)

element1=[1,2,5,6,7]
element2=[1,2,3,5,6,7]
element3=[1,2,3,5,6,7]

troba(element1,element2,element3)