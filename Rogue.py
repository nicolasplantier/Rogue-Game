from xxlimited import new
import pygame as pg 

pg.init() #pour initialiser pygame 

DIRECTIONS = {
    "DOWN": (0, +1),
    "UP": (0, -1),
    "RIGHT": (+1, 0),
    "LEFT": (-1, 0),
}

#character_color = (0,200,0) (vert)

class character:
    def __init__(self, position, direction): #position = liste de 2 coordonnées [x,y] #direction = un tupple du dictionnaire DIRECTIONS
        self.position = position 
        self.direction = direction 
    
    def set_direction(self,direction):
        if direction in DIRECTIONS: 
            self.direction = direction 
    
    def move(self):
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
            



#attention pour le couloir : on y entre par une porte et après on ne peut que avancer dans le couloir 
#ie. il faut que la case new_position soit une case couloir ou une case porte qui permet de sortir du couloir


#comment on repère une case ? 
#400 x 400 pixels et une case = 20 pixel donc quand on donne les coordonnées (15,15) ça correspond à 15x20... 
#matrice 20 x 20 pour chaque case 