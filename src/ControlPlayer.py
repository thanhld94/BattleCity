from Player import *
from Environment import *

# Manually control player with keyboard
# Import the matrix board from environment - see Environment.py for details
# Movements:
#    j: left
#    k: down
#    i: up
#    l: right

class ControlPlayer(Player):
   
    def __init__(self, env):
        #contructor - manually
        self.dx = [1, -1, 0, 0]
        self.dy = [0, 0, 1,-1]
        self.environment = env
        self.map = {'i':1, 'k':0, 'l':2, 'j':3}
        self.setup(1,2)

    def setup(self, row, col):
        self.pos_row = row
        self.pos_col = col
        self.direction = 0;

    def shoot(self):
        print("Fired")
        return

    def validMove(self, direction):
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
        print(str(inputMove))
        if inputMove == ' ':
            self.shoot()
            return
        self.direction = self.map[inputMove]
        if self.validMove(self.direction):
            next_row = (self.pos_row + self.dx[self.direction]) % len(self.environment.board)
            next_col = (self.pos_col + self.dy[self.direction]) % len(self.environment.board[0])
            print("Original pos: "+str(self.pos_row)+" "+str(self.pos_col))
            self.row = next_row
            self.col = next_col
            print("New pos: "+str(self.row)+" "+str(self.col));
        return 

#Test functions
env = Environment()        
player = ControlPlayer(env)
player.move()
            
        
