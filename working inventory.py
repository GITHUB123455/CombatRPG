from weapons import Sword, Club, Fists
from consumables import HealthPotion, StrengthPotion, VampirismAntidote

def findInList(item, listOfItems):
  for i, sublist in enumerate(listOfItems):
    if item in sublist:
      return i
  return -1

weapons = {'sword' : Sword, 'club' : Club, 'fists' : Fists}
consumables = {'health potion' : HealthPotion,'strength potion' : StrengthPotion 'vampirism antidote' : VampirismAntidote}

class Inventory(object):
  def __init__(self):
    self.equippedWeapon = Fists()
    self.weapons = []
    self.consumables = [[" ", 0] for i in range(len(consumables))]

    for i, consumable in enumerate(consumables):
      self.consumables[i][0] = consumable

    self.finalAttackBonus = 0
    self.consumedItem = None

  def displayWeapons(self):
    print("Weapons:")
    for i in self.weapons:
      print(i)

  def displayConsumables(self):
    print("Consumables:")
    x = 0
    for i in range(len(self.consumables)):
      if self.consumables[i][1] != 0:
        print(self.consumables[i][0] + "(x" + str(self.consumables[i][1]) + ")")
        x += 1
    if x == 0:
      print('You have no consumables in your inventory.')


  def equipWeapon(self):
    selection = input("Select the weapon you would like to equip. ").lower()
    try:
      tmp = self.equippedWeapon.name
      self.equippedWeapon = weapons[selection]()
      self.weapons[self.weapons.index(selection)] = tmp
      self.finalAttackBonus = self.equippedWeapon.attackBonus
      print('You have equipped your ' + selection + '.')
    except KeyError:
      print('Exiting inventory.')
      return
    except ValueError:
      print('Exiting inventory.')
      return

  def useConsumable(self):
    self.displayConsumables()
    selection = input("Select the consumable you would like to use. ").lower()
    try:
      if self.consumables[findInList(selection, self.consumables)][1] > 0:
        self.consumedItem = consumables[selection]()
        self.consumables[findInList(selection, self.consumables)][1] -= 1
        print('You have consumed a ' + selection + '.')
        return
      else:
        return

    except KeyError:
      print('Exiting inventory')
      return

  def consumableEffect(self):
    try:
      if self.consumedItem.duration > 0:
        self.consumedItem.duration -= 1
        if self.consumedItem.statBonus == "Health":
          print('Health increased by ' + str(self.consumedItem.bonusAmount) + '.')
          return "Health", self.consumedItem.bonusAmount
      elif self.consumedItem.statBonus == "Strength":
          print('Strength increased by ' + str(self.consumedItem.bonusAmount) + '.')
          return "Strength", self.consumedItem.bonusAmount
      elif self.consumedItem.statBonus == "Cure":
          print('You are cured of your vampiritis.')
          return "Cure", self.consumedItem.bonusAmount
      else:
        self.consumedItem = None
        print('No Bonus')
        return " ", 0

    except AttributeError:
      return " ", 0

    except TypeError:
        return " ", 0
