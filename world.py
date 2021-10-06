import random
import player

class WorldSpace(object):
  worldBiomes = ['Giant Mushroom Forest', 'Tornado-Ravaged Desert', 'Misterious Forest','Bleak Tundra', 'Ancient Jungle']

  enemies = [[' ', 5], ['orc', 5], ['goblin', 5], ['dragon', 5], ['vampire', 5]]

  consumables = [[' ', 5], ['health potion', 5], ['vampirism antidote', 5], ['stamina potion', 5], ['super strength potion', 5], ['strength potion', 5]]



  def __init__(self, scale):
      self.scale = scale
      self.Night = False
      self.ProbobilitySum(self.enemies)
      self.ProbobilitySum(self.consumables)



  def worldGen(self):

    self.world_array = [[0]*self.scale for i in range(self.scale)]
    self.enemy_array = [[0]*self.scale for i in range(self.scale)]
    self.drops_array = [[[0 for cool in range(2)]for cool in range(self.scale)]for cool in range(self.scale)]

  def terrainGen(self):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        self.world_array[i][p] = random.randrange(100)
    self.terrainAssignment()

  def terrainAssignment(self):
    for i in range(int(self.scale)):
        for p in range(int(self.scale)):
            self.world_array[i][p] = self.worldBiomes[int(int(self.world_array[i][p])/20)]

  def enemyGeneration(self, player):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        if i == player.x and p == player.y:
          self.enemy_array[i][p] = 0.0
        else:
          self.enemy_array[i][p] = random.uniform(0.0, 100.0)
    self.enemyAssignment()
    # for i in range(10):
    #   for p in range(10):
    #     print (self.enemy_array[i][p])

  def enemyAssignment(self):
    for i in range(int(self.scale)):
        for p in range(int(self.scale)):
            for j in range(len(self.enemies)):
                if self.enemies[j][1] >= self.enemy_array[i][p]:
                    self.enemy_array[i][p] = self.enemies[j][0]
                    break

  def consumablesGen(self):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        self.drops_array[i][p][1] = random.randrange(100)
    self.consumablesAssignment()

  def consumablesAssignment(self):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        for j in range(2):
            for k in range(len(self.consumables)):
                if self.consumables[k][1] >= self.drops_array[i][p][j]:
                    self.drops_array[i][p][j] = self.consumables[k][0]
                    break

  def getTerrain(self, player):
    return self.world_array[player.x][player.y]

  def getEnemy(self, player):
    return self.enemy_array[player.x][player.y]

  def clearEnemy(self, player):
    self.enemy_array[player.x][player.y] = ' '
    return

  def DayNight(self):
    self.TimeCounter += 1
    if self.TimeCounter > 5:
       self.Night = True
       print('Night time is here be prepared!')
    elif self.TimeCounter <= 5:
       print ("The sun is up, Day has arrived")
    elif self.TimeCounter == 11:
       self.TimeCounter = 0

  def ProbobilitySum(self, array):
      Sum = 0.0
      for i in range(len(array)):
          Sum += array[i][1]
      for i in range(len(array)):
          if i == 0:
              array[i][1] = 100.0 * array[i][1]/Sum
          else:
              array[i][1] = (100.0 * array[i][1]/Sum) + array[i-1][1]
