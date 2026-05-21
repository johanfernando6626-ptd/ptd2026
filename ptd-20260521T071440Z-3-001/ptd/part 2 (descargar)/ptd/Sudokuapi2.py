import requests

def llegeixSudoku():
    x = requests.get('https://sudoku-api.vercel.app/api/dosuku')
    #print(x.text)
    dades = x.json()
    print(dades["newboard"]["grids"][0]["solution"])
    #sudoku=dades["newboard"]["grids"][0]["solution"]
    return dades

def llegeixSudokuN():
    x = requests.get('https://sudoku-api.vercel.app/api/dosuku')
    print(x.text)
    dades = x.json()

    print(dades["newboard"]["grids"][0]["value"])
    return dades["newboard"]["grids"][0]["value"]


def imprimeixSudoku(s):
    for i in s:
        print(i)

def comprovaSudoku():
    
    #retorna true si el valor és un grup de sudoku és correcte
    #grup: linia, columna, quadrat
    #El grup ha de tenir tots els nombres i no repetirne cap.
    print("S'ha de fer el algoritme.")

###----------------------------------------------
#def contarzeros():
#    print("contaré zeros")
#    n = 0
#    for n in range(len(taula)):
#        
#    return n
###----------------------------------------------
sortir=False

sudoku=[]
sudokuN=[]

while not sortir:   
    print("*************************************")
    print("BENVINGUDES AL COMPROVADOR DE SUDOKUS")
    print("*************************************")
    print("1. Comprovar el sudoku")
    print("2. Mostrar el sudoku")
    print("3. Llegir el sudoku resolt")
#    print("4. Llegir un nou sudoku no resolt")
    print("4. Llegir quants zeros hi ha")
    print("0. Sortir")
    print("*************************************")
    opcio = input("Introdueix una opció: ")
    if opcio == "1":
        comprovaSudoku()
    elif opcio == "2":
        print("SUDOKU NO RESOLT")
        imprimeixSudoku(sudokuN)
        print("SUDOKU RESOLT")
        imprimeixSudoku(sudoku)
    elif opcio == "3":
        dades = llegeixSudoku()
        print(dades["newboard"]["grids"][0]["solution"])
        print(dades["newboard"]["grids"][0]["value"])


        print("S'ha llegit un nou sudoku resolt")
    
#    elif opcio == "4":
#        zeros = contarzeros()
#        print("S'ha contat el numero total de zeros", zeros)

#elif opcio == "4":
#sudokuN = llegeixSudokuN()
#print("S'ha llegit un nou sudoku no resolt")

        
    elif opcio == "0":
        sortir=True

print("Fins aviat!")


#afegir opció 4---Fer copy paste/ Funció que conti zeros