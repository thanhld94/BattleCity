# Create the matrix board
class Environment:
  
  def __init__(self):
    self.EMPTY = 0
    self.BRICK = 1
    self.WATER = 2
    self.BASE  = 3
    self.board = [
      [2,1,0,0,0,0,0,0,1,2],
      [2,1,0,0,1,1,0,0,1,2],
      [2,1,0,0,1,1,0,0,1,2],
      [2,1,0,0,1,1,0,0,1,2],
      [0,0,0,1,0,0,1,0,0,2],
      [2,1,0,2,2,2,2,0,1,2],
      [2,1,0,1,1,1,1,0,1,2],
      [2,1,0,0,0,0,0,0,1,2],
      [2,1,0,1,1,1,0,0,1,2],
      [2,1,0,1,3,1,0,0,1,2]
    ]

  def updateCell (self, row, col, newState):
    self.board[row][col] = newState


