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
        self.enemy = enemy
        self.p1 = player
        #create window
        self.win = GraphWin()
        self.win.setCoords(0,0,30,30)
        self.prev_enemy_pos = Rectangle(Point(0,0),Point(0,0))
        self.prev_p1_pos = Rectangle(Point(0,0),Point(0,0))
    def update(self, environment, enemy, player):
        self.env = environment
        self.enemy = enemy
        self.p1 = player
    def drawMap(self):
        self.win.update()
        # Legend information
        # -Water
        water = Rectangle (Point(22, 0), Point(24, 2))
        water.draw(self.win)
        water.setFill("blue")
        waterSign = Text(Point(25,1), "Water")
        waterSign.draw(self.win)
        # - Brick
        brick = Rectangle (Point(22, 2), Point(24, 4))
        brick.draw(self.win)
        brick.setFill("brown")
        brickSign = Text(Point(25,3), "Brick")
        brickSign.draw(self.win)
        # - Base
        base = Rectangle (Point(22, 4), Point(24, 6))
        base.draw(self.win)
        base.setFill("yellow")
        baseSign = Text(Point(25,5), "Base")
        baseSign.draw(self.win)
        # Delete this polygon if use other map than the 10x10 matrix
        p = Polygon(Point(0,0), Point(0, 20), Point(20,20), Point(20,0))
        p.setWidth(4)
        p.draw(self.win)
        #draw map
        for row in range (0, len(self.env.board)*2, 2):
            for col in range (0, len(self.env.board[0])*2, 2):
                # clear previous position of player and enemy
                self.prev_enemy_pos.undraw()
                self.prev_p1_pos.undraw()
                # locate the position of enemy
                if (self.enemy.pos_row == int(row/2) and self.enemy.pos_col == int(col/2)):
                  self.prev_enemy_pos = Rectangle(Point(row, col), Point(row+2, col+2));   
                  rec = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec.draw(self.win)
                  rec.setFill("black")
                # position of player
                if (self.p1.pos_row == int(row/2) and self.p1.pos_col == int(col/2)):
                  self.prev_p1_pos = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec.draw(self.win)
                  rec.setFill("green")
                # if the cell is empty
                if (self.env.board[int(row/2)][int(col/2)] == 0):
                  rec = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec.draw(self.win)
                elif (self.env.board[int(row/2)][int(col/2)] == 1):
                  #if the cell is brick
                  rec = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec.draw(self.win)
                  rec.setFill("brown")
                elif (self.env.board[int(row/2)][int(col/2)] == 2):
                  #if the cell is water
                  rec = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec.draw(self.win)
                  rec.setFill("blue")
                elif (self.env.board[int(row/2)][int(col/2)] == 3):
                  rec = Rectangle(Point(row, col), Point(row+2, col+2));
                  rec.draw(self.win)
                  rec.setFill("yellow")



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
