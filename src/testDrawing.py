import time, os, sys
from zellegraphics import *
from Environment import *

def myTest():
  win = GraphWin()
  win = setCoordis(0,0,50,50)
  t = Text(Point(5,5), "Centered Tet")
  t.draw(win)
  p = Polygon(Point(1,1), Point(1, 11), Point(11,1), Point(11,11))
  p.draw(win)
  win.close()

env = Environment()

def test():
    win = GraphWin()
    win.setCoords(0,0,30,30)
    p = Polygon(Point(0,0), Point(0, 20), Point(20,20), Point(20,0))
    p.setWidth(4)
    p.draw(win)
    
    for row in range (0, 20, 2):
      for col in range(0, 20, 2):
        # if the cell is empty
        if (env.board[int(row/2)][int(col/2)] == 0):
          rec = Rectangle(Point(row, col), Point(row+2, col+2));
          rec.draw(win)
        elif (env.board[int(row/2)][int(col/2)] == 1):
          #if the cell is brick
          rec = Rectangle(Point(row, col), Point(row+2, col+2));
          rec.draw(win)
          rec.setFill("brown")
        elif (env.board[int(row/2)][int(col/2)] == 2):
          #if the cell is water
          rec = Rectangle(Point(row, col), Point(row+2, col+2));
          rec.draw(win)
          rec.setFill("blue")
        else:
          rec = Rectangle(Point(row, col), Point(row+2, col+2));
          rec.draw(win)
          rec.setFill("yellow")

    #for i in range (2, 23, 2):
#      l = Polygon(Point(1,i), Point(21,i))
#      for j in range (1, 23, 2):
#        c = Polygon(Point(j, 2), Point(j, 22))
#        c.draw(win)
#      l.draw(win)

  
    #rec = Rectangle (Point(1, 1), Point(3, 3))
    #rec.draw(win)

    

if __name__ == "__main__":
    test()
