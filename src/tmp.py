class Tmp:
  def __init__(self):
    self.amap = {'i': 0, 'j': 1, 'k':2, 'l':3}

  def doit(self):
    self.shoot()
    letter = input("Input: ")
    direction = self.amap[letter]
    print("direction = " + str(direction))

  def shoot(self):
    print("shot fired")

x = Tmp()
x.doit()
