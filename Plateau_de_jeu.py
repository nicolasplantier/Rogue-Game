import pygame as pg

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

class Board_Game:
    def __init__(self, walls, corridors, doors, rooms):
        self.walls = walls #liste des coordonnées des cases avec des murs
        self.corridors = corridors
        self.doors = doors
        self.rooms = rooms
        #self.character = character #de class Character
    
    def color(self):
        for wall in self.walls:
            draw_tile(screen, wall[0], wall[1], RED)
        for corridor in self.corridors:
            draw_tile(screen, corridor[0], corridor[1], GREY)
        for door in self.doors:
            draw_tile(screen, door[0], door[1], ORANGE)
        for room in self.rooms:
            draw_tile(screen, room[0], room[1], WHITE)
        #character = self.character
        #draw_tile(screen, character.position[0], character.position[1], GREEN)


pg.init()
screen = pg.display.set_mode((400, 400)) #1 case = 20x20 pixels

running = True
while running:
    clock.tick(1)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    board = Board_Game(walls, corridors, doors, rooms)
    board.color()
    pg.display.update()
