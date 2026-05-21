import requests
def llegeixSudokuN():
    x = requests.get('https://sudoku-api.vercel.app/api/dosuku')
    print(x.text)
    dades = x.json()

    print(dades["newboard"]["grids"][0]["value"])
    return dades["newboard"]["grids"][0]["value"]
