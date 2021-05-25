from weapons import Sword, Club, Fists
from consumables import HealthPotion, StrengthPotion, SuperStrengthPotion, StaminaPotion, VampireCure

def FindInList(Item, ListOfItems):
  for i, Sublist in enumerate(ListOfItems):
    if Item in Sublist:
      return i
  return -1

weapons = {'sword' : Sword, 'club' : Club, 'fists' : Fists}
consumables = {'health potion' : HealthPotion, 'strength potion' : StrengthPotion, 'super strength potion' : SuperStrengthPotion, 'stamina potion' : StaminaPotion, 'vampirism antidote' : VampireCure}

class Inventory(object):
  def __init__(self):
    self.equippedWeapon = Fists()
    self.weapons = []
    self.consumables = [[" ", 0] for i in range(len(consumables))]

    for i, consumable in enumerate(consumables):
      self.consumables[i][0] = consumable

    self.finalAttackBonus = 0
    self.consumedItem = [None] * len(consumables)

  def displayWeapons(self):
    print("weapons:")
    for i in self.weapons:
      print(i)

  def displayConsumables(self):
    print("consumables:")
    x = 0
    for i in range(len(self.consumables)):
      if self.consumables[i][1] != 0:
        print(self.consumables[i][0] + "(x" + str(self.consumables[i][1]) + ")")
        x += 1
    if x == 0:
      print("You have no consumables in your inventory.")

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
        if self.consumables[FindInList(selection, self.consumables)][1] > 0:
            for Slot in self.consumedItem:
                if self.consumedItem[Slot] is None:
                    self.consumedItem[Slot] = consumables[selection]()
            self.consumables[FindInList(selection, self.consumables)][1] -= 1
            print('You have consumed a ' + selection + '.')
            return
        else:
            return

    except KeyError:
      print('Exiting inventory')
      return

    # except ValueError:
    #   print('Exiting inventory.')
    #   return

  def ConsumablEffect(self):
      for Slot in self.consumedItem:

          try:
                if self.consumedItem[Slot].duration > 0:
                    self.consumedItem[Slot].duration -= 1
                    if self.consumedItem[Slot].statBonus == "Health":
                        print('Health increased by ' + str(self.consumedItem[Slot].bonusAmount) + '.')
                        return "Health", self.consumedItem[Slot].bonusAmount
                    elif self.consumedItem[Slot].statBonus == "Strength":
                        print('Strength increased by' + str(self.consumedItem[Slot].bonusAmount))
                        return "Strength", self.consumedItem[Slot].bonusAmount
                    elif self.consumedItem[Slot].statBonus == "SuperStrength":
                        print('Strength increased by' + str(self.consumedItem[Slot].bonusAmount))
                        return "Strength", self.consumedItem[Slot].bonusAmount
                    elif self.consumedItem[Slot].statBonus == "Stamina":
                        print('Stamina increased' + str(self.consumedItem[Slot].bonusAmount))
                        return "Stamina", self.consumedItem[Slot].bonusAmount
                else:
                    self.consumedItem[Slot] = None
                    print('No bonus')
                    return " ", 0

          except AttributeError:
              return " ", 0

          except TypeError:
              return " ", 0
