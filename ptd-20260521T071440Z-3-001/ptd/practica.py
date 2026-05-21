import pygame
import requests
import sys

pygame.init()

# -----------------------------
# CONFIG
# -----------------------------
WIDTH, HEIGHT =  510, 700 #500, 600 540, 650
CELL_SIZE = WIDTH // 9

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GRAY = (200,200,200)
BLUE = (100,100,255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku MVC")

font = pygame.font.SysFont("Arial", 21)

# -----------------------------
# CLASSE CASELLA
# -----------------------------
class Casella:
    def __init__(self, row, col, value=0):
        self.row = row
        self.col = col
        self.value = value
        self.selected = False

    def draw(self, screen):
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE

        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

        # color selecció
        if self.selected:
            pygame.draw.rect(screen, RED, rect)
        else:
            pygame.draw.rect(screen, WHITE, rect)

        pygame.draw.rect(screen, BLUE, rect, 1)

        if self.value != 0:
            text = font.render(str(self.value), True, BLACK)
            screen.blit(text, (x+20, y+35))

    def handle_key(self, key):
        if self.selected:
            if pygame.K_1 <= key <= pygame.K_9:
                self.value = key - pygame.K_0
            elif key == pygame.K_BACKSPACE:
                self.value = 0

# -----------------------------
# CLASSE BOTO
# -----------------------------
class Boto:
    def __init__(self, x, y, w, h, text, action):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.action = action

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)
        label = font.render(self.text, True, BLACK)
        screen.blit(label, (self.rect.x+5, self.rect.y+10))

    def handle_click(self, pos):
        if self.rect.collidepoint(pos):
            self.action()

# -----------------------------
# MODEL
# -----------------------------
class SudokuModel:
    def __init__(self):
        self.grid = [[Casella(i,j) for j in range(9)] for i in range(9)]
        self.solution = None

    def load_api(self):
        try:
            r = requests.get("https://sudoku-api.vercel.app/api/dosuku")
            data = r.json()

            grid = data["newboard"]["grids"][0]

            for i in range(9):
                for j in range(9):
                    self.grid[i][j].value = grid["value"][i][j]

            self.solution = grid["solution"]

        except:
            print("Error carregant API")

# -----------------------------
# VISTA
# -----------------------------
class SudokuView:
    def draw(self, screen, model, buttons):
        screen.fill(GRAY)

        

        # dibuixar caselles
        for row in model.grid:
            for cell in row:
                cell.draw(screen)

        # línies gruixudes
        for i in range(0,10,3):
            pygame.draw.line(screen, BLACK, (0,i*CELL_SIZE),(WIDTH,i*CELL_SIZE),3)
            pygame.draw.line(screen, BLACK, (i*CELL_SIZE,0),(i*CELL_SIZE,WIDTH),3)

        # botons
        for b in buttons:
            b.draw(screen)

        pygame.display.flip()

# -----------------------------
# CONTROLADOR
# -----------------------------
class SudokuController:
    def __init__(self, model):
        self.model = model

    def select_cell(self, pos):
        x,y = pos
        if y < WIDTH:
            row = y // CELL_SIZE
            col = x // CELL_SIZE

            for r in self.model.grid:
                for c in r:
                    c.selected = False

            self.model.grid[row][col].selected = True

    def handle_key(self, key):
        for row in self.model.grid:
            for cell in row:
                cell.handle_key(key)

    # BOTONS
    def load(self):
        self.model.load_api()

    def comprovaGrup(self,grup):
        print("El grup es:",grup)
        tots = [1,2,3,4,5,6,7,8,9]
    
        for i in range(len(grup)):
            #print("El valor de tots és ", grup[i])
            if (grup[i] in tots):
                tots.remove(grup[i])
            #print("Llista grup:", grup )
            #print("Llista tots:", tots )
    
        if len(tots) == 0:
            return True
        else:
            return False

    def check(self):
        print("Funció comprova.")
        #hem d'enviar les 89 files, 9 columnes i 9 grups
        
        llista=[]

        for i in range (3):
          for j in range (3):
            llista.append(self.model.grid[j][i].value)
        if self.comprovaGrup(llista):
          print("GRUP0 ", i, " ", j, "correcte")
        else:
          print("GRUP0 ", i, " ", j, "incorrecte")
        
        llista=[]
        for i in range (3):
          for j in range (3,6):
            llista.append(self.model.grid[j][i].value)
        if self.comprovaGrup(llista):
          print("GRUP1 ", i, " ", j, "correcte")
        else:
          print("GRUP1 ", i, " ", j, "incorrecte")
      
        llista=[]
        for i in range (3):
          for j in range (6,9):
            llista.append(self.model.grid[j][i].value)
        if self.comprovaGrup(llista):
          print("GRUP3 ", i, " ", j, "correcte")
        else:
          print("GRUP3 ", i, " ", j, "incorrecte")
      
        
        for i in range (0,9):
          llista=[]
          for j in range (0,9):
            llista.append(self.model.grid[i][j].value)
          if self.comprovaGrup(llista):
            print("fila ", i, " ", j, "correcte")
          else:
            print("fila ", i, " ", j, "incorrecte")
        
        for i in range (0,9):
          llista=[]
          for j in range (0,9):
            llista.append(self.model.grid[j][i].value)
          if self.comprovaGrup(llista):
            print("fila ", i, " ", j, "correcte")
          else:
            print("fila ", i, " ", j, "incorrecte")
            
        
            

    def show_result(self):
        if self.model.solution:
            for i in range(9):
                for j in range(9):
                    self.model.grid[i][j].value = self.model.solution[i][j]

    def solve(self):
        self.backtracking()

    def u(self):
        
        for i in range (9):
            for j in range (9):
                self.model.grid[i][j].value = 1

    def contar(self):
        
            for i in range(9):
                for j in range(9):

                    n = self.model.grid[0][0].value
            print("*-----------------------------------*")
            print("contaré quantes vegades apareix:",n)
            
            print("*-----------------------------------*")
            return n.count()


    def missatge(self, missatge):
        pass

    '''
def(lista, numero_a_buscar):
    """Cuenta cuántas veces aparece un número en una lista."""
    return lista.count(numero_a_buscar)

# Ejemplo de uso
mi_lista = [1, 5, 2, 1, 3, 1, 4, 5]
numero = 1
resultado = contar_apariciones(mi_lista, numero)
print(f"El número {numero} aparece {resultado} veces.") # Salida: 3 veces
'''
   

    def copia(self):
        
        for i in range (9):
            for j in range (9):
                self.model.grid[i][j].value = self.model.grid[0][0].value

    
    def Hinf(self):
       
        
        n = self.model.grid[0][0].value
        

        for i in range (9):
            for j in range (9):
                n += 1
                self.model.grid[i][j].value = n
                

    
    # BACKTRACKING
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.model.grid[i][j].value == 0:
                    return i,j
        return None

    def valid(self, num, row, col):
        for j in range(9):
            if self.model.grid[row][j].value == num:
                return False

        for i in range(9):
            if self.model.grid[i][col].value == num:
                return False

        box_x = col//3
        box_y = row//3

        for i in range(box_y*3, box_y*3+3):
            for j in range(box_x*3, box_x*3+3):
                if self.model.grid[i][j].value == num:
                    return False

        return True

    def backtracking(self):
        empty = self.find_empty()
        if not empty:
            return True

        row,col = empty

        for num in range(1,10):
            if self.valid(num,row,col):
                self.model.grid[row][col].value = num
                if self.backtracking():
                    return True
                self.model.grid[row][col].value = 0

        return False

# -----------------------------
# MAIN
# -----------------------------
model = SudokuModel()
view = SudokuView()
controller = SudokuController(model)

buttons = [
    Boto(10,520,490,40,"si", controller.missatge),
    Boto(10,640,120,50,"Carrega", controller.load),
    Boto(140,640,120,50,"Comprova", controller.check),
    Boto(270,640,120,50,"Resultat", controller.show_result),
    Boto(400,640,120,50,"Resol", controller.solve),
    Boto(10,580,120,50,"Tot és 1", controller.u),
    Boto(270,580,120,50,"Copia [0],[0]", controller.copia),
    Boto(140,580,120,50,"Continua", controller.Hinf),
    Boto(400,580,120,50,"Quants", controller.contar),
]


running = True
while running:

    view.draw(screen, model, buttons)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            controller.select_cell(pos)

            for b in buttons:
                b.handle_click(pos)

        elif event.type == pygame.KEYDOWN:
            controller.handle_key(event.key)

pygame.quit()
sys.exit()