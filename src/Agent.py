from Player import *
from Environment import *
from Bullet import *
from DeepNet import *

class Agent(Player):

  def __init__(self, env, bullets):
    # constructor
    self.dx = [1, -1, 0, 0] # up, down, right, left
    self.dy = [0, 0, 1, -1] # up, down, right, left
    self.environment = env
    self.bullets = bullets
    # setting the DeepNet running session
    self.sess = tf.Session()
    self.sess.run(tf.initialize_all_variables())  
    self.model = model

  def setup(self, row, col, player):
    # setup initial position and direction
    self.pos_row = row
    self.pos_col = col
    self.player = player
    self.direction = 0 # default down

  def move(self):
    moveToMake = self.getPrediction()
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

  # Predict the next move using DeepNet 
  # and return the move index
  def getPrediction(self):
    features = self.getFeaturesVector()
    predictions = self.sess.run(self.model, feed_dict={x: features})[0]
    resultMove = 0
    for i in range(len(predictions)):
      if predictions[i] > predictions[resultMove]:
        resultMove = i
    return resultMove

  # Return the corresponding state into a features vector
  # [[18 features]]
  def getFeaturesVector(self):
    pass
