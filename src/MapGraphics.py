'''
    Map Graphics draws the map from the matrix
    in the Environment.py
'''
import time, os, sys
from third_parties.zellegraphics import *
from Environment import *
from Enemy import *
from Dummy import *
from ControlPlayer import *

class MapGraphics:

    def __init__(self, environment, enemy, player):
        self.env = environment
        self.matrix = [[Rectangle(Point(0,0), Point(0,0)) for j in range (0, len(self.env.board[0])*2)] for i in range (0, len(self.env.board)*2)]
        self.enemy = enemy
        self.p1 = player
        #create window
        self.win = GraphWin()
        self.win.setCoords(0,0,30,30)
        # Delete this polygon if use other map than the 10x10 matrix
        p = Polygon(Point(0,0), Point(0, 20), Point(20,20), Point(20,0))
        p.setWidth(1)
        p.draw(self.win)
        self.prev_enemy_pos = []
        self.prev_enemy_pos.append(self.enemy.pos_row)
        self.prev_enemy_pos.append(self.enemy.pos_col)
        self.prev_p1_pos = []
        self.prev_p1_pos.append(self.p1.pos_row)
        self.prev_p1_pos.append(self.p1.pos_col)
                
    def update(self, environment, enemy, player):
        self.prev_enemy_pos[0]= self.enemy.pos_row
        self.prev_enemy_pos[1]= self.enemy.pos_col
        self.prev_p1_pos[0]= self.p1.pos_row
        self.prev_p1_pos[1]= self.p1.pos_col
        self.env = environment
        self.enemy = enemy
        self.p1 = player

    # drawMap main points:
    # Check each cell of the matrix and redraw and change color of each cell base
    # on the difference between old and new update environment
    # Future test: did not test the case in which the brick cell is delete because of bullet collision
    def drawMap(self):
        self.win.update()
        # delete old position of enemy and player
        self.matrix[self.prev_enemy_pos[0]*2][self.prev_enemy_pos[1]*2].setFill("white")
        self.matrix[self.prev_p1_pos[0]*2][self.prev_p1_pos[1]*2].setFill("white")
        for row in range (0, len(self.env.board)*2, 2):
            for col in range (0, len(self.env.board[0])*2, 2):
                # locate the position of enemy
                if (self.enemy.pos_row == int(row/2) and self.enemy.pos_col == int(col/2)):
                   self.matrix[row][col] = Rectangle(Point(row, col), Point(row+2, col+2))
                   self.matrix[row][col].draw(self.win)
                   self.matrix[row][col].setFill("black")
                # position of player
                if (self.p1.pos_row == int(row/2) and self.p1.pos_col == int(col/2)):
                   self.matrix[row][col] = Rectangle(Point(row, col), Point(row+2, col+2))
                   self.matrix[row][col].draw(self.win)
                   self.matrix[row][col].setFill("green")
                # if the cell is empty
                if (self.env.board[int(row/2)][int(col/2)] == 0):
                   self.matrix[row][col] = Rectangle(Point(row, col), Point(row+2, col+2))
                   self.matrix[row][col].draw(self.win)
                elif (self.env.board[int(row/2)][int(col/2)] == 1):
                # if cell is brick
                   self.matrix[row][col] = Rectangle(Point(row, col), Point(row+2, col+2))
                   self.matrix[row][col].draw(self.win)
                   self.matrix[row][col].setFill("brown")
                elif (self.env.board[int(row/2)][int(col/2)] == 2):
                #if the cell is water
                   self.matrix[row][col] = Rectangle(Point(row, col), Point(row+2, col+2))
                   self.matrix[row][col].draw(self.win)
                   self.matrix[row][col].setFill("blue")
                elif (self.env.board[int(row/2)][int(col/2)] == 3):
                   self.matrix[row][col] = Rectangle(Point(row, col), Point(row+2, col+2))
                   self.matrix[row][col].draw(self.win)
                   self.matrix[row][col].setFill("yellow")


#test
#env = Environment()
#bullets_1 = []
#bullets_2 = []
#p1 = Enemy(env, bullets_1) 
#enemy = Enemy(env, bullets_2)
#p1.setup(2,7,enemy)
#enemy.setup(2,2, p1)
#battleGround = MapGraphics(env, enemy, p1)
#i = 10
#while (i>=0):
#    battleGround.drawMap()
#    i = i - 1
#battleGround.drawMap()
