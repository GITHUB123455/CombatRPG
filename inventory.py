from weapons import Sword, Club, Fists
from armour import RustyIronArmour, NewIronArmour
from consumables import HealthPotion, StrengthPotion, SuperStrengthPotion, StaminaPotion, VampireCure

def FindInList(Item, ListOfItems):
  for i, Sublist in enumerate(ListOfItems):
    if Item in Sublist:
      return i
  return -1

weapons = {'sword' : Sword, 'club' : Club, 'fists' : Fists}
armours = {'rusty iron armour' : RustyIronArmour, 'new iron armour' : NewIronArmour}
consumables = {'health potion' : HealthPotion, 'strength potion' : StrengthPotion, 'super strength potion' : SuperStrengthPotion, 'stamina potion' : StaminaPotion, 'vampirism antidote' : VampireCure}

class Inventory(object):
  def __init__(self):
    self.equippedWeapon = Fists()
    self.weapons = []
    self.consumables = [[" ", 0] for i in range(len(consumables))]
    self.equippedArmour = RustyIronArmour()
    self.armour = [[" ", 0] for i in range(len(armours))]
    for i, consumable in enumerate(consumables):
      self.consumables[i][0] = consumable
    for i, armour in enumerate(armours):
      self.armour[i][0] = armour

    self.finalAttackBonus = 0
    self.consumedItem = [None] * len(consumables)

  def displayWeapons(self):
    print("weapons:")
    for i in self.weapons:
      print(i)

  def displayArmour(self):
    print("consumables:")
    x = 0
    for i in range(len(self.armour)):
      if self.armour[i][1] != 0:
        print(self.armour[i][0] + "(x" + str(self.armour[i][1]) + ")")
        x += 1
    if x == 0:
      print("You have no armour in your inventory.")

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
  def equipArmour(self):
      self.displayArmour()
      selection = input("Select the armour you would like to equip. ").lower()
      tmp = self.equipArmour
      try:
          if self.armour[FindInList(selection, self.armour)][1] > 0:
              self.armour[FindInList(selection, self.armour)][1] -= 1
              print('You have equipped your ' + selection + '.')
              self.equippedArmour = selection
              self.armour[FindInList(tmp, self.armour)][1] += 1
              return
          else:
              return

      except KeyError:
        print('Exiting inventory')
        return

  def useConsumable(self):
    self.displayConsumables()
    selection = input("Select the consumable you would like to use. ").lower()
    Flag = 0
    try:
        if self.consumables[FindInList(selection, self.consumables)][1] > 0:
            for Slot in range(len(self.consumedItem)):
                if self.consumedItem[Slot] is None and Flag == 0:
                    self.consumedItem[Slot] = consumables[selection]()
                    Flag = 1
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
      PotionType = [ ]
      BonusAmount = [ ]
      for Slot in range(len(self.consumedItem)):
          if self.consumedItem[Slot] is None:
              PotionType.append(" ")
              BonusAmount.append(0)

          elif self.consumedItem[Slot].duration > 0:
                    self.consumedItem[Slot].duration -= 1
                    if self.consumedItem[Slot].statBonus == "Health":
                        print('Health increased by ' + str(self.consumedItem[Slot].bonusAmount) + '.')
                        PotionType.append("Health")
                        BonusAmount.append(self.consumedItem[Slot].bonusAmount)
                    elif self.consumedItem[Slot].statBonus == "Strength":
                        print('Strength increased by ' + str(self.consumedItem[Slot].bonusAmount))
                        PotionType.append("Strength")
                        BonusAmount.append(self.consumedItem[Slot].bonusAmount)
                    elif self.consumedItem[Slot].statBonus == "Stamina":
                        print('Stamina increased by ' + str(self.consumedItem[Slot].bonusAmount))
                        PotionType.append("Stamina")
                        BonusAmount.append(self.consumedItem[Slot].bonusAmount)
          else:
                    self.consumedItem[Slot] = None
                    print('No bonus')
                    PotionType.append(" ")
                    BonusAmount.append(0)

      return PotionType, BonusAmount
