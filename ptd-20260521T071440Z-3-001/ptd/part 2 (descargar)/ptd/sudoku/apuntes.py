print("COMPROVANT COLUMNES")
for i in range(9):
    for j in range(9):
        columna.append(sudoku[j][i])
    print("columna ", i, ": ",columna)
    comprovaGrup(columna)
    columna=[]
print("COMPROVANT FILES")
for i in range(9):
    for j in range(9):
        fila.append(sudoku[i][j])
    print("fila ", i, ": ",fila)
    comprovaGrup(fila)
    fila=[]



            fila.append(sudoku[0][0])
        fila.append(sudoku[0][1])
        fila.append(sudoku[0][2])

        fila.append(sudoku[1][0])
        fila.append(sudoku[1][1])
        fila.append(sudoku[1][2])

        fila.append(sudoku[2][0])
        fila.append(sudoku[2][1])
        fila.append(sudoku[2][2])
        print (fila)
    print ("grup", i,": ",)
    #print (i,j+(n%3))