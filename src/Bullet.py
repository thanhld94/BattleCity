class Bullet:

  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.direction = direction
    # up, down, left, right
    global dx, dy
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

  def move(self):
    self.x += dx[self.direction]
    self.y += dy[self.direction]

  def __str__(self):
    return "pos = " + str(self.x) + ", " + str(self.y) + " dir = " + str(self.direction)
