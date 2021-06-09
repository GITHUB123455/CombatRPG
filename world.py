import random
import player

class WorldSpace(object):
  worldBiomes = ['Giant Mushroom Forest', 'Tornado-Ravaged Desert', 'Misterious Forest','Bleak Tundra', 'Ancient Jungle']

  enemies = [' ', 'orc', 'goblin', 'dragon', 'vampire']

  consumables = [' ', 'health potion', 'vampirism anitidote', 'stamina potion', 'super strength potion', 'strength potion']

  EnemySpawnFrequency = [20, 10, 5, 5]

  EnemyProbability = {}
  def __init__(self, scale):
      self.scale = scale
      self.Night = False
      EnemyProbability = ProbabilityGen(enemies, EnemySpawnFrequency)


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
          self.enemy_array[i][p] = 0
        else:
          self.enemy_array[i][p] = random.randrange(100)
    self.enemyAssignment()
    # for i in range(10):
    #   for p in range(10):
    #     print (self.enemy_array[i][p])

  def enemyAssignment(self):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        if int(self.enemy_array[i][p]) > 95:
          self.enemy_array[i][p] = self.enemies[3]
        elif int(self.enemy_array[i][p]) > 80:
          self.enemy_array[i][p] = self.enemies[4]
        elif int(self.enemy_array[i][p]) > 68:
          self.enemy_array[i][p] = self.enemies[1]
        elif int(self.enemy_array[i][p]) > 50:
          self.enemy_array[i][p] = self.enemies[2]
        else:
          self.enemy_array[i][p] = self.enemies[0]

  def consumablesGen(self):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        self.drops_array[i][p][1] = random.randrange(100)
    self.consumablesAssignment()

  def consumablesAssignment(self):
    for i in range(int(self.scale)):
      for p in range(int(self.scale)):
        for j in range(2):
          if int(self.drops_array[i][p][j])> 90:
            self.drops_array[i][p][j] = self.consumables[2]
          elif int(self.drops_array[i][p][j]) > 80:
            self.drops_array[i][p][j] = self.consumables[4]
          elif int(self.drops_array[i][p][j]) > 60:
            self.drops_array[i][p][j] = self.consumables[1]
          elif int(self.drops_array[i][p][j]) > 40:
            self.drops_array[i][p][j] = self.consumables[3]
          elif int(self.drops_array[i][p][j]) > 20:
            self.drops_array[i][p][j] = self.consumables[5]

          else:
            self.drops_array[i][p][j] = self.consumables[0]

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
       print ("The sun is up, Day is here")
    elif self.TimeCounter == 11:
       self.TimeCounter = 0

  def ProbabilityGen(self, list, chance):
      ProbabilityDictionary = { }
      Empty = 0
      for i in range(len(chance)):
          Empty += chance[i]
      Empty = 100 - Empty
      chance.insert(0, Empty)
      for i in range(len(chance)):
          chance[i + 1] += chance[i]
      for i in range(len(chance)):
          ProbabilityDictionary[chance[i]] = list[i]
      return ProbabilityDictionary
