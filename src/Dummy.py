from Player import *
from Environment import *

class Dummy(Player):
  def __init__(self):
    self.setup(0,2)

  def setup(self, row, col):
    self.pos_row = row
    self.pos_col = col
  
  def move(self):
    print("I moved, but not really")
