import random

class Enemy(object):
  def lightAttack(self):
    self.stamina -= 1
    return random.randrange(1, 20) + (self.strength/2), random.randrange(1, 8) + (self.strength/2)

  def heavyAttack(self):
    self.stamina -= 2
    return random.randrange(1, 20) + (self.strength/2), random.randrange(1, 8) + (self.strength)

  def attack(self, player):
    if self.health / self.maxhealth <= 0.5:
      print('The ' + self.type + ' is bloodied.')

    if self.stamina >= 3 and random.randrange(100) > 83:
      print('The ' + self.type + ' special attacks.')
      return self.specialAttack(player)

    elif self.stamina >= 2 and random.randrange(100) > 68:
      print('The ' + self.type + ' attacks.')
      return self.heavyAttack()

    elif self.stamina >= 1 and random.randrange(100) > 20:
      print('The ' + self.type + ' attacks.')
      return self.lightAttack()

    else:
      self.stamina += 2
      print('The ' + self.type + ' rests.')
      return 0, 0

  def dropItem(self):
    return self.dropTable[random.randrange(len(self.dropTable))]

class Orc(Enemy):
  def __init__(self):
    self.type = 'orc'
    self.health = 30
    self.maxhealth = self.health
    self.dexterity = 2
    self.strength = 6
    self.armorClass = 14
    self.stamina = 10
    self.dropTable = [' ', ' ', ' ', 'club']

  def specialAttack(self, player):
    self.stamina -= 3
    return random.randrange(1, 20) + (self.strength), random.randrange(1, 8) + (self.strength) + 4

class Goblin(Enemy):
  def __init__(self):
    self.type = 'goblin'
    self.health = 20
    self.maxhealth = self.health
    self.dexterity = 4
    self.strength = 1
    self.armorClass = 11
    self.stamina = 7
    self.dropTable = [' ', ' ', ' ', 'club']

  def specialAttack(self, player):
    self.stamina -= 3
    return random.randrange(1, 20) + (self.strength/2), random.randrange(1, 8) + (self.strength)

class Dragon(Enemy):
  def __init__(self):
    self.type = 'dragon'
    self.health = 90
    self.maxhealth = self.health
    self.dexterity = 3
    self.strength = 20
    self.armorClass = 19
    self.stamina = 50
    self.dropTable = ['sword', 'club']

  def specialAttack(self, player):
    self.stamina -= 3
    player.burning = True
    player.burnDuration = random.randrange(1, 3)
    return random.randrange(1, 30) + (self.strength), random.randrange(1, 8) + (self.strength) * 2

class Vampire(Enemy):
  def __init__(self):
    self.type = 'vampire'
    self.health = 90
    self.maxhealth = self.health
    self.dexterity = 3
    self.strength = 20
    self.armorClass = 19
    self.stamina = 50
    self.dropTable = ['sword']

  def specialAttack(self, player):
    self.stamina -= 3
    if random.randrange(100) >= 89:
      player.infected = True
      player.infectedDuration = random.randrange(15, 20)
      print('You have contracted vampiritis.')
    return random.randrange(1, 30) + (self.strength), random.randrange(1, 8) + (self.strength) * 2
