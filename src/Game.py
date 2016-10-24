import time
from Environment import *
from Enemy import *
from Dummy import *
from ControlPlayer import *

env = Environment()
#p1 = Dummy()
p1 = ControlPlayer(env)
enemy = Enemy(env, p1)
enemy.setup(9, 6)
enemy.move()

def print_board(env, p1, p2):
  state = {0: ' ', 1: '#', 2: '~', 3: '$'}
  for row in range(len(env.board)):
    print("+", end="")
    for col in range(len(env.board[0])):
      print("---+", end="")
    print()
    print("|", end="")
    for col in range(len(env.board[0])):
      cell = state[env.board[row][col]]
      if p1.pos_row == row and p1.pos_col == col:
        cell = 'P'
      elif p2.pos_row == row and p2.pos_col == col:
        cell = 'E'
      print(" " + cell + " |", end="")
    print()
  print("+", end="")
  for col in range(len(env.board[0])):
    print("---+", end="")
  print()

for idx in range(20):
  print_board(env, p1, enemy)
  enemy.move()
  p1.move()
