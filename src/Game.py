import time
from Environment import *
from Enemy import *
from Dummy import *
from ControlPlayer import *

env = Environment()
#p1 = Dummy()
bullets_1 = []
bullets_2 = []
p1 = ControlPlayer(env, bullets_1)
enemy = Enemy(env, p1, bullets_2)
enemy.setup(1,10)

def print_board(env, p1, p2, bullets_1, bullets_2):
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
      else:
        for bullet in bullets_1:
          if bullet.row == row and bullet.col == col:
            cell = '.'
        for bullet in bullets_2:
          if bullet.row == row and bullet.col == col:
            cell = '.'
      print(" " + cell + " |", end="")
    print()
  print("+", end="")
  for col in range(len(env.board[0])):
    print("---+", end="")
  print()

while (1):
  gameover = False
  for bullet in bullets_1:
    bullet.move()
    if bullet.row < 0 or bullet.row >= len(env.board) or bullet.col < 0 or bullet.col >= len(env.board[0]):
      bullets_1.remove(bullet)
      continue
    if env.board[bullet.row][bullet.col] == env.BRICK:
      env.updateCell(bullet.row, bullet.col, env.EMPTY)
      bullets_1.remove(bullet)
      continue
    if env.board[bullet.row][bullet.col] == env.BASE:
      env.updateCell(bullet.row, bullet.col, env.EMPTY)
      bullets_1.remove(bullet)
      gameover = True
      print("GAMEOVER!")
      break
    if enemy.pos_row == bullet.row and enemy.pos_col == bullet.col:
      env.updateCell(bullet.row, bullet.col, env.EMPTY)
      bullets_1.remove(bullet)
      gameover = True
      print("VICTORY!")
      break
  if gameover:
    break

  for bullet in bullets_2:
    bullet.move()
    if bullet.row < 0 or bullet.row >= len(env.board) or bullet.col < 0 or bullet.col >= len(env.board[0]):
      bullets_2.remove(bullet)
      gameover = True
      continue
    if env.board[bullet.row][bullet.col] == env.BRICK:
      env.updateCell(bullet.row, bullet.col, env.EMPTY)
      bullets_2.remove(bullet)
      continue
    if env.board[bullet.row][bullet.col] == env.BASE:
      env.updateCell(bullet.row, bullet.col, env.EMPTY)
      bullets_2.remove(bullet)
      gameover = True
      print("GAMEOVER!")
      break
    if p1.pos_row == bullet.row and p1.pos_col == bullet.col:
      env.updateCell(bullet.row, bullet.col, env.EMPTY)
      bullets_2.remove(bullet)
      gameover = True
      print("GAMEOVER!")
      break
  if gameover:
    break
  print_board(env, p1, enemy, bullets_1, bullets_2)
  enemy.move()
  p1.move()
  
