from random import choice

#rooms = []
room1 = []
room2 = []
room3 = []
room4 = []
for x in range(1, 6):
    for y in range(1, 14):
        room4.append([x, y])
for x in range(11, 15):
    for y in range(14, 18):
        room3.append([x, y])
for x in range(11, 17):
    for y in range(6, 9):
        room2.append([x, y])
for x in range(12, 17):
    for y in range(1, 3):
        room1.append([x, y])
rooms = room1 + room2 + room3 + room4

class Near_Position():
    def __init__(self, character, room_number = 0, room = []):
        self.room_number = room_number
        self.position = character.position
        self.room = room
    
    def is_in_room(self):
        if self.position in room1:
            self.room_number = 1
            self.room = room1
        if self.position in room2:
            self.room_number = 2
            self.room = room2
        if self.position in room3:
            self.room_number = 3
            self.room = room3
        if self.position in room4:
            self.room_number = 4
            self.room = room4
        return self.room_number, self.room
    
    def near_pos(self, character):
        self.room = self.is_in_room()
        accessible_pos = [pos for pos in self.room if character.position != pos]
        self.position = choice(accessible_pos)
        return self.position


#Classe nouvellement définie

class Food:
    def __init__(self, life_score = 5, position = food_initial_pos, counter = 0):
        self.life_score = life_score
        self.position = position
        self.counter = counter
    
    def place_food(self, board_game):
        r = NearPosition()
        self.position = r.near_pos(board_game.character)
        #accessible_pos = [room for room in board_game.rooms if board_game.character.position != room]
        #self.position = choice(accessible_pos)
    
    def print_food(self):
        pg.draw.circle(screen, GREEN, (self.position[0]*W + 10, self.position[1]*H + 10), 8)
    
    def eating(self, board_game, money):
        if board_game.character.position == self.position:
            self.counter = 0
            if self.life_score < 5:
                self.life_score += 1
            self.place_food(board_game)
        else:
            self.counter += 1
            if self.counter == 7:
                self.life_score -= 1
                self.counter = 0
        if self.life_score == 0:
            print(f"Game Over : Mort de faim avec {money.score} pièces")
            pg.quit()
            exit()
        pg.display.set_caption(f"Life Score : {self.life_score}")
        self.print_food()