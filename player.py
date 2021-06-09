import random
from inventory import Inventory

class Player(object):
    def __init__(self, x, y, playerMaxDist):
      #Location and movment
      self.x = x
      self.y = y
      self.directions = dict(w=(0,-1), s=(0,1), d=(1,0), a=(-1,0))
      self.playerMaxDist = playerMaxDist

      #Stats
      self.maxHealth = 35
      self.maxStamina = 10
      self.dexterity = 3
      self.strength = 6
      self.armorClass = 14

      #Placeholder Stats
      self.health = self.maxHealth
      self.stamina = self.maxStamina

      #Conditions
      self.burning = False
      self.burnDuration = 0
      self.paralyzed = False
      self.paralyzeDuration = 0
      self.Infected = False
      self.InfectedTime = 0

      self.inventory = Inventory()

      self.counter = 0


    def movement(self):
      self.counter += 1

      if self.Infected:
         self.infectedAction()

      print('W. | North')
      print('S. | South')
      print('D. | East')
      print('A. | West')
      movementInput = input("Input the direction you would like to travel. ").lower()
      #Compare it to the dictionary of moves
      if movementInput in self.directions:
          #Move
          direction = self.directions[movementInput]
          self.x, self.y = self.x + direction[0], self.y + direction[1]
          self.worldBounds()
      else:
          #Return exception
          print('Invalid Input')

    #Checks the player location against the world bounds and makes
    #sure the player does not leave the map
    def worldBounds(self):
        if self.x >= self.playerMaxDist:
            self.x = self.playerMaxDist - 1
            print("You have gone too far, turning you around.")
        if self.x < 0:
            self.x = 0
            print("You have gone too far, turning you around.")
        if self.y >= self.playerMaxDist:
            self.y = self.playerMaxDist - 1
            print("You have gone too far, turning you around.")
        if self.y < 0:
            self.y = 0
            print("You have gone too far, turning you around.")

    def attack(self):
      #Apply Conditions
      self.ApplyPotions()

      if self.burning:
        self.burningAction()

      if self.paralyzed:
        self.paralyzedAction()
        return 0, 0

      print('1. Light Attack')
      print('2. Heavy Attack')
      print('3. Rest')
      print('4. Drink Potion')
      attacktype = input('Input the attack you would like to make. ').lower()
      if attacktype == '1' or attacktype == 'light' or attacktype == 'light attack':
        if self.stamina >= 1:
          print('You light attack.')
          self.stamina -= 1
          return random.randrange(1, 20) + (self.strength/2), random.randrange(1, 8) + (self.strength/2) + self.inventory.finalAttackBonus
        else:
          print('Not enough stamina! You rest.')
          self.stamina += 1
          return 0,0
      if attacktype == '2' or attacktype == 'heavy' or attacktype == 'heavy attack':
        if self.stamina >= 2:
          print('You heavy attack.')
          self.stamina -= 2
          return random.randrange(1, 20) + (self.strength/2), random.randrange(1, 8) + (self.strength) + self.inventory.finalAttackBonus
        else:
          print('Not enough stamina! You rest.')
          self.stamina += 1
          return 0, 0
      if attacktype == '3':
        print('You rest.')
        self.stamina += 2
        if self.stamina > self.maxStamina:
            self.stamina = self.maxStamina
            print('You are fully energized.')
        return 0, 0
      if attacktype == '4':
        self.inventory.useConsumable()
        return 0,0
      else:
        print('Invalid input.')
        return self.attack()

    def burningAction(self):
      if self.burnDuration > 0:
        self.health -= 5
        self.burnDuration -= 1
      else:
        self.burning = False

    def paralyzedAction(self):
      if self.paralyzeDuration <= 0:
        self.paralyzed = False
      else:
        self.paralyzeDuration -= 1

    def infectedAction(self):
      if self.InfectedTime <= 0:
        self.Infected = False
      else:
        self.InfectedTime -= 1

    def checkInventory(self):
      self.inventory.displayConsumables()
      if len(self.inventory.weapons) > 0:
        self.inventory.displayWeapons()
        self.inventory.equipWeapon()
      else:
        print('You have no weapons in your inventory.')
        return

    def decision(self):
      print("1. Move")
      print("2. Inventory")
#      print("3. Stats")
      selection = input('What would you like to do? ').lower()

      if selection == '1' or selection == 'move':
        self.movement()

      elif selection == '2' or selection == 'inventory':
        self.checkInventory()

#      elif selection == '3' or selection == 'stats':
#        print('Your Health : ' + str(player.health))
#        print('Your Stamina : ' + str(player.stamina))
#         print('Vampire Satus: ' + InfectedStatus)
      else:
        print('Invalid input')

    def getDrops(self, world):
      return world.drops_array[self.x][self.y][0], world.drops_array[self.x][self.y][1]

    def pickupDrops(self, world, type):
      droppedItem = world.drops_array[self.x][self.y][type]
      if droppedItem == ' ':
        return
      print('You found a ' + droppedItem + '.')
      playerChoice = input('Would you like to pick it up? ').lower()
      if playerChoice == 'yes':
        if type == 0:
          self.inventory.weapons.append(droppedItem)
        elif type == 1:
          for k in range(len(self.inventory.consumables)):
              if self.inventory.consumables[k][0] == droppedItem:
                  self.inventory.consumables[k][1] += 1
        print('You picked up the ' + droppedItem + '.')
        world.drops_array[self.x][self.y][type] = ' '
        return
      elif playerChoice == 'no':
        print('You decided to move on.')
        return
      else:
        print('Invalid input.')

    def ApplyPotions(self):
        PotionType, BonusAmount = self.inventory.ConsumablEffect()
        for Place in range(len(PotionType)):
            if PotionType[Place] == "Health":
                self.health += BonusAmount[Place]
                if self.health > self.maxHealth:
                    self.health = self.maxHealth
                print("Your health: " + str(self.health))
            elif PotionType[Place] == "Stamina":
                self.stamina += BonusAmount[Place]
                if self.stamina > self.maxStamina:
                    self.stamina = self.maxStamina
                print("Your stamina: " + str(self.stamina))
            elif PotionType[Place] == "Strength":
                self.strength += BonusAmount[Place]
                print("Your strength: " + str(self.strength))
            elif PotionType[Place] == "Cure":
                self.Infected = False
                self.InfectedTime = 0
