import random
from Player import *
from Environment import *
from Bullet import *

class Enemy(Player):

  def __init__(self, env, bullets):
    # constructor
    self.dx = [1, -1, 0, 0] # up, down, right, left
    self.dy = [0, 0, 1, -1] # up, down, right, left
    self.environment = env
    self.bullets = bullets

  def setup(self, row, col, player):
    # setup initial position and direction
    self.pos_row = row
    self.pos_col = col
    self.player = player
    self.direction = 0 # default down

  def move(self):
    # make a move
    if self.encounter_enemy():
      # if encounter an enemy then shoot
      self.shoot()
      return
    validMoves = self.getPossibleMoves()
    # if we are not in a tunnel then randomize the next move
    next_dir = self.getRandomDir(validMoves)
    self.direction = next_dir
    self.pos_row = (self.pos_row + self.dx[next_dir]) % len(self.environment.board)
    self.pos_col = (self.pos_col + self.dy[next_dir]) % len(self.environment.board[0])

  def validMove(self, direction):
    # check if a move in the direction is valid
    # a move is valid if it is not a wall or water
    # a move can wrap around
    next_row = (self.pos_row + self.dx[direction]) % len(self.environment.board)
    next_col = (self.pos_col + self.dy[direction]) % len(self.environment.board[0])
    if self.environment.board[next_row][next_col] == self.environment.WATER:
      return False
    if self.environment.board[next_row][next_col] == self.environment.BASE:
      return False
    if self.environment.board[next_row][next_col] == self.environment.BRICK:
      return False
    return True
    
  def getRandomDir(self, possible):
    # getting a random valid direction
    idx = random.randrange(0, len(possible), 1)
    return possible[idx]

  def getPossibleMoves(self):
    # get a list of possible moves
    possible = []
    for direction in range(4):
      if self.validMove(direction):
        possible.append(direction)
    if self.validMove(self.direction):
      last = len(possible) * 5
      for idx in range(last):
        possible.append(self.direction)
    return possible


  def encounter_enemy(self):
    # check if there is a player in the direction we are in
    r = self.pos_row
    c = self.pos_col
    while r >= 0 and r < len(self.environment.board) and c >= 0 and c < len(self.environment.board[0]):
      if self.environment.board[r][c] == self.environment.BRICK:
        return False
      if r == self.player.pos_row and c == self.player.pos_col:
        return True
      r = r + self.dx[self.direction]
      c = c + self.dy[self.direction]
    return False

  def shoot(self):
    # fire a shot, add bullet to the bullet list
    self.bullets.append(Bullet(self.pos_row, self.pos_col, self.direction))
    return
