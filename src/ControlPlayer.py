from Player import *
from Environment import *
from Bullet import *
# Manually control player with keyboard
# Import the matrix board from environment - see Environment.py for details
# Movements:
#    j: left
#    k: down
#    i: up
#    l: right

class ControlPlayer(Player):
   
    def __init__(self, env, bullets):
        #contructor - manually
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1,-1]
        self.environment = env
        self.map = {'i':1, 'k':0, 'l':2, 'j':3}
        self.setup(1,2)
        self.bullets = bullets

    def setup(self, row, col):
        self.pos_row = row
        self.pos_col = col
        self.direction = 0;

    def shoot(self):
        # create and append new bullet to the list
        self.bullets.append(Bullet(self.pos_row, self.pos_col, self.direction));
        return

    def validMove(self, direction):
        # check the next move against environmental obstacles
        next_row = (self.pos_row + self.dx[self.direction]) % len(self.environment.board)
        next_col = (self.pos_col + self.dy[self.direction]) % len(self.environment.board[0])
        if self.environment.board[next_row][next_col] == self.environment.WATER:
            print("Hit water")
            return False
        if self.environment.board[next_row][next_col] == self.environment.BASE:
            print("Hit base")
            return False
        if self.environment.board[next_row][next_col] == self.environment.BRICK:
            print("Hit brick")
            return False
        return True
    
    def move(self):
        inputMove = input("Enter direction: ")
        # Test print move - delete afterward
        print(str(inputMove))
        if inputMove == ' ':
            self.shoot()
            return
        self.direction = self.map[inputMove]
        if self.validMove(self.direction):
            next_row = (self.pos_row + self.dx[self.direction]) % len(self.environment.board)
            next_col = (self.pos_col + self.dy[self.direction]) % len(self.environment.board[0])
            print("Original pos: "+str(self.pos_row)+" "+str(self.pos_col))
            self.pos_row = next_row
            self.pos_col = next_col
            print("New pos: "+str(self.pos_row)+" "+str(self.pos_col));
        return 
