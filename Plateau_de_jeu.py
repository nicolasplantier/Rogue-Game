import pygame as pg
from random import choice

# Constants
# --------------------------------------------------------------------------------------------------

#Nombre de pixels par case
W = 20
H = 20

#Nombre de cases
X = 20
Y = 20

#Couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (160, 0, 0)
ORANGE = (255, 127, 0)
GREY = (100, 100, 100)
GREEN = (0, 160, 0)
BLUE = (0, 0, 160)

#Plateau fixe
doors = [[15, 3], [15, 5], [14, 9], [14, 13], [10, 17], [3, 14]]
corridors = [[15, 4], [14, 10], [14, 11], [14, 12], [9, 17], [8, 17], [7, 17], [6, 17], [5, 17], [4, 17], [3, 17], [3, 16], [3, 15]]
rooms = []
for x in range(1, 6):
    for y in range(1, 14):
        rooms.append([x, y])
for x in range(11, 15):
    for y in range(14, 18):
        rooms.append([x, y])
for x in range(11, 17):
    for y in range(6, 9):
        rooms.append([x, y])
for x in range(12, 17):
    for y in range(1, 3):
        rooms.append([x, y])
walls = []
for x in range(0, 7):
    walls.append([x, 0])
for y in range(0, 15):
    walls.append([0, y])
    walls.append([6, y])
for x in range(10, 16):
    walls.append([x, 18])
for y in range(13, 19):
    walls.append([15, y])
for y in range(5, 10):
    walls.append([10, y])
    walls.append([17, y])
for y in range(4):
    walls.append([11, y])
    walls.append([17, y])
for x in range(11, 18):
    walls.append([x, 0])
wall_bis = [[1, 14], [2, 14], [4, 14], [5, 14], [10, 13], [10, 14], [10, 15], [10, 16], [11, 13], [12, 13], [13, 13], [11, 9], [12, 9], [13, 9], [15, 9], [16, 9], [17, 9], [11, 5], [12, 5], [13, 5], [14, 5], [16, 5], [17, 5], [12, 3], [13, 3], [14, 3], [16, 3]]
walls += wall_bis

#Directions
DIRECTIONS = {
    "DOWN": (0, +1),
    "UP": (0, -1),
    "RIGHT": (+1, 0),
    "LEFT": (-1, 0),
    #"NO_MOVE": (0, 0)
}

#Première pièce
money_initial_pos = [14, 2]

# --------------------------------------------------------------------------------------------------



clock = pg.time.Clock()



def draw_tile(screen, x, y, color):
    """
    colorier la case d'abcisse x, ordonnée y en la couleur color
    """
    rect = pg.Rect(x*W, y*H, W, H)
    pg.draw.rect(screen, color, rect)

def draw_background(screen):
    screen.fill(BLACK)


class Character:
    def __init__(self, position, direction): #position = liste de 2 coordonnées [x,y] #direction = un tupple du dictionnaire DIRECTIONS
        self.position = position 
        self.direction = direction 
    
    def set_direction(self,direction):
        if direction in DIRECTIONS: 
            self.direction = DIRECTIONS[str(direction)]
    
    def move(self, board_game):
        x, y = self.position[0], self.position[1]
        dx, dy = self.direction 
        new_position = [x+dx, y+dy] 
        if new_position in board_game.walls: #le personnage ne peut pas traverser les murs 
            print("Attention au mur")
            #self.position = self.position #le personnage reste à sa position 
        elif self.position in board_game.corridors: #si le personnage est dans un couloir, il ne peut pas sortir du couloir (il est forcé de suivre le chemin défini par le couloir)
            if (new_position in board_game.corridors) or (new_position in board_game.doors):
                self.position = new_position #le perso avance dans le couloir ou sort du couloir par la porte 
            else:
                print("Tu ne peux pas sortir du couloir")
        else:
            self.position = new_position

class Board_Game:
    def __init__(self, walls, corridors, doors, rooms, character):
        self.walls = walls #liste des coordonnées des cases avec des murs
        self.corridors = corridors
        self.doors = doors
        self.rooms = rooms
        self.character = character #de class Character
    
    def color(self):
        for wall in self.walls:
            draw_tile(screen, wall[0], wall[1], RED)
        for corridor in self.corridors:
            draw_tile(screen, corridor[0], corridor[1], GREY)
        for door in self.doors:
            draw_tile(screen, door[0], door[1], ORANGE)
        for room in self.rooms:
            draw_tile(screen, room[0], room[1], WHITE)
        character = self.character
        draw_tile(screen, character.position[0], character.position[1], GREEN)

class Money:
    def __init__(self, score = 0, position = money_initial_pos):
        self.score = score
        self.position = position
    
    def get_money(self):
        self.score += 1
    
    def place_money(self, board_game):
        accessible_pos = [room for room in board_game.rooms if board_game.character.position != room]
        self.position = choice(accessible_pos)

    def print_money(self):
        pg.draw.circle(screen, BLUE, (self.position[0]*W + 10, self.position[1]*H + 10), 8)
    
    def gain_money(self, board_game):
        #for _ in range(5):
        if board_game.character.position == self.position:
            self.get_money()
            self.place_money(board_game)
        self.print_money()
        pg.display.set_caption(f"Score : {self.score}")


pg.init()
screen = pg.display.set_mode((400, 400)) #1 case = 20x20 pixels

character = Character([16, 0], (0, 1))
running = True
board = Board_Game(walls, corridors, doors, rooms, character)
money = Money()
money.gain_money(board)
while running:
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN:
                character.set_direction("DOWN")
            if event.key == pg.K_UP:
                character.set_direction("UP")
            if event.key == pg.K_RIGHT:
                character.set_direction("RIGHT")
            if event.key == pg.K_LEFT:
                character.set_direction("LEFT")
        #else:
            #character.set_direction("NO_MOVE")
    character.move(board)
    board = Board_Game(walls, corridors, doors, rooms, character)
    board.color()
    money.gain_money(board)
    pg.display.update()
