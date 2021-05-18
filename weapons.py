class Weapons(object):
  def getAttackBonus(self):
    return self.attackBonus()

class Fists(Weapons):
  def __init__(self):
    self.name = 'fists'
    self.attackBonus = 0

class Sword(Weapons):
  def __init__(self):
    self.name = 'sword'
    self.attackBonus = 2

class Club(Weapons):
  def __init__(self):
    self.name = 'club'
    self.attackBonus = 3