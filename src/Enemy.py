import random
from Player import *
from Environment import *

class Enemy(Player):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  def __init__(self, env, player):
    # constructor
    self.environemnt = env
    self.player = player

  def setup(self, row, col):
    # setup initial position and direction
    self.pos_row = row
    self.pos_col = col
    self.direction = 0 # default down

  def move(self):
    # make action 
    if encounter_enemy():
      shoot()
      return
    if validMove(self.direction):
      next_row = (pos_row + dx[self.direction]) % len(self.environemnt.board)
      next_col = (pos_col + dy[self.direction]) % len(self.environemnt.board[0])
      self.row = next_row
      self.col = next_col
      return
    next_dir = getRandomDir()
    self.row = (pos_row + dx[next_dir]) % len(self.environemnt.board)
    self.col = (pos_col + dy[next_dir]) % len(self.environemnt.board[0])

  def validMove(self, direction):
    next_row = (pos_row + dx[self.direction]) % len(self.environemnt.board)
    next_col = (pos_col + dy[self.direction]) % len(self.environemnt.board[0])
    if self.environemnt.board[next_row][next_col] == Environment.WATER:
      return False
    if self.environemnt.board[next_row][next_col] == Environment.BASE:
      return False
    if self.environemnt.board[next_row][next_col] == Environment.BRICK:
      return False
    return True
    
  def getRandomDir(self):
    # getting a random valid direction
    possible = []
    for direction in range(4):
      if validMove(direction):
        possible.append(direction)
    return possible[random.randrage(0, len(possible), 1)]

  def encounter_enemy(self):
    r = self.pos_row
    c = self.pos_col
    while r >= 0 and r < len(self.environemnt.board) and c >= 0 and c <= len(self.environemnt.board[0]):
      if self.environment.board[r][c] == BRICK:
        return False
      if r == self.player.pos_row and c == self.player.pos_col:
        return True
      r = r + dx[self.direction]
      c = c + dy[self.direction]
    return False

  def shoot(self):
    # fire a shot
    # do nothing
    print("shot fired!")
    return
