import random

class Consumable(object):
  def __init__(self):
    self.duration
    self.statBonus
    self.bonusAmount

class HealthPotion(Consumable):
  def __init__(self):
    self.duration = 1
    self.statBonus = "Health"
    self.bonusAmount = random.randrange(1, 6) * 3

class StrengthPotion(Consumable):
    def __init__(self):
        self.duration = random.randrange(1,3)
        self.statBonus = "Strength"
        self.bonusAmount = random.randrange(1,3) * 3

class VampirismAntidote(Consumable):
    def __init__(self):
        self.duration = 1
        self.statBonus = "Cure"
        self.bonusAmount = 0
