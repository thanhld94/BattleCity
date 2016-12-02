from Player import *
from Environment import *
from Bullet import *
from DeepNet import *
from Enemy import *
import math

class Agent(Player):

  def __init__(self, env, bullets, enemies):
    # constructor
    self.dx = [1, -1, 0, 0] # up, down, right, left
    self.dy = [0, 0, 1, -1] # up, down, right, left
    self.environment = env
    self.bullets = bullets
    self.enemies = enemies;
    # setting the DeepNet running session
    self.neuralNet = DeepNet("../training_data/sorted_data.in", "../training_data/sorted_data.out")
    self.neuralNet.train(10000)

  def setup(self, row, col, player):
    # setup initial position and direction
    self.pos_row = row
    self.pos_col = col
    self.player = player
    self.direction = 0 # default down

  def move(self):
    moveToMake = self.neuralNet.predict(self.getFeaturesVector())
    # shooting action
    if moveToMake == 4:
      self.shoot()
      return
    if not self.validMove(moveToMake):
      return
    self.direction = moveToMake
    self.pos_row = (self.pos_row + self.dx[moveToMake]) % len(self.environment.board)
    self.pos_col = (self.pos_col + self.dy[moveToMake]) % len(self.environment.board[0])

  # fire a shot, add bullet to the bullet list
  def shoot(self):
    print("Shot fired")
    self.bullets.append(Bullet(self.pos_row, self.pos_col, self.direction))
    return
  
  # check if a move in the direction is valid
  # a move is valid if it is not a wall or water
  # a move can wrap around
  def validMove(self, direction):
    next_row = (self.pos_row + self.dx[direction]) % len(self.environment.board)
    next_col = (self.pos_col + self.dy[direction]) % len(self.environment.board[0])
    if self.environment.board[next_row][next_col] == self.environment.WATER:
      return False
    if self.environment.board[next_row][next_col] == self.environment.BASE:
      return False
    if self.environment.board[next_row][next_col] == self.environment.BRICK:
      return False
    return True

  # Return the corresponding state into a features vector
  # [[18 features]]
  def getFeaturesVector(self):
    currentState = [];
    # position of the agent
    currentState.append(self.pos_row)
    currentState.append(self.pos_col)
    # agent's current direction
    currentState.append(self.direction)

    # enemy distance
    minEnemies = [math.inf, math.inf, math.inf, math.inf]
    for enemy in self.enemies: 
      distEnemies = max(abs(self.pos_row - enemy.pos_row), abs(self.pos_col - enemy.pos_col))
      if (self.pos_col == enemy.pos_col):
        # if enemy is found on the same column
        # find if the enemy is above or below 
        if (self.pos_row < enemy.pos_row):
          # the enemy is below of agent
          minEnemies[1] = min(distEnemies, minEnemies[1])
        else:
          # the enemy is above
          minEnemies[0] = min(distEnemies, minEnemies[0])
      elif (self.pos_row == enemy.pos_row):
        # the enemy is found on the same row
        # find if the enemy is on the left or right of agent
        if (self.pos_col < enemy.pos_col):
          # the enemy is on the right of agent
          minEnemies[3] = min(distEnemies, minEnemies[3])
        else:
          # the bullets is on the left of agent
          minEnemies[2] = min(distEnemies, minEnemies[2])
    # update min distance of enemy
    for val in minEnemies:
      currentState.append(val)

    # bullet distance
    minBullets = [math.inf, math.inf, math.inf, math.inf]
    for bullet in self.bullets: 
      distBullet = max(abs(self.pos_row - bullet.row), abs(self.pos_col - bullet.col))
      if (self.pos_col == bullet.col):
        # if bullet is found on the same column
        # find if the bullet is above or below 
        if (self.pos_row < bullet.row):
          # the bullet is below of agent
          minBullets[1] = min(distBullet, minBullets[1])
        else:
          # the bullet is above
          minBullets[0] = min(distBullet, minBullets[0])
      elif (self.pos_row == bullet.row):
        # the bullet is found on the same row
        # find if the bullet is on the left or right of agent
        if (self.pos_col < bullet.col):
          # the bullet is on the right of agent
          minBullets[3] = min(distBullet, minBullets[3])
        else:
          # the bullets is on the left of agent
          minBullets[2] = min(distBullet, minBullets[2])
    
    # update min distance of bullet
    for val in minBullets:
      currentState.append(val)

    # available movement
    for step in range (0, 4):
      if (self.validMove(step)):
        currentState.append(1)
      else:
        currentState.append(0)

    #base information
    currentState.append(self.environment.baseState[0])
    currentState.append(self.environment.baseState[1])
    currentState.append(self.environment.baseState[2])

    return currentState



