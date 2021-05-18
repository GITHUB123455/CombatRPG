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
    self.duration = 1
    self.statBonus = "Strength"
    self.bonusAmount = random.randrange(1, 4) * 2

class SuperStrengthPotion(Consumable):
  def __init__(self):
    self.duration = 1
    self.statBonus = "SuperStrength"
    self.bonusAmount = random.randrange(1, 10) * 5

class StaminaPotion(Consumable):
  def __init__(self):
    self.duration = 1
    self.statBonus = "Stamina"
    self.bonusAmount = random.randrange(1, 4) * 2

class VampireCure(Consumable):
  def __init__(self):
    self.duration = 1
    self.statBonus = "Cure"
    self.bonusAmount = 0
