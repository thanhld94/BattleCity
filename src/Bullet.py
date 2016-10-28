class Bullet:

  def __init__(self, row, col, direction):
    self.row = row
    self.col = col
    self.direction = direction
    # up, down, left, right
    global dx, dy
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

  def move(self):
    self.row += dx[self.direction]
    self.col += dy[self.direction]
