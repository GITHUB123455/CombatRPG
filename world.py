import random

class WorldSpace(object):
    worldBiomes = ['Giant Mushroom Forest', 'Tornado-Ravaged Desert', 'Forest','Bleak Tundra', 'Ancient Jungle']

    enemies = [[' ',5],['orc',5], ['goblin',5], ['dragon',5], ['vampire',5]]

    consumables = [[' ',5], ['health potion',5], ['vampirism antidote',5]]


    def __init__(self, scale):
        self.scale = scale
        self.time = 0
        self.night = False
        self.probSum(self.enemies)
        self.probSum(self.consumables)

    def worldGen(self):
        self.world_array = [[0]*self.scale for i in range(self.scale)]
        self.enemy_array = [[0]*self.scale for i in range(self.scale)]
        self.drops_array = [[[0 for col in range(2)] for col in range(self.scale)] for row in range(self.scale)]

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
              self.enemy_array[i][p] = random.uniform(0.0,100.0)
        self.enemyAssignment()

    def enemyAssignment(self):
        for i in range(int(self.scale)):
          for p in range(int(self.scale)):
              print(self.enemy_array[i][p])
        for i in range(int(self.scale)):
          for p in range(int(self.scale)):
              for j in range(len(self.enemies)):
                  if self.enemies[j][1] >= self.enemy_array[i][p]:
                      self.enemy_array[i][p] = self.enemies[j][0]
                      break
        for i in range(int(self.scale)):
          for p in range(int(self.scale)):
              print(self.enemy_array[i][p])

    def consumablesGen(self):
        for i in range(int(self.scale)):
          for p in range(int(self.scale)):
            for j in range(2):
              self.drops_array[i][p][1] = random.uniform(0.0,100.0)
        self.consumablesAssignment()

    def consumablesAssignment(self):
        for i in range(int(self.scale)):
          for p in range(int(self.scale)):
            for j in range(2):
                for k in range(len(self.consumables)):
                    if self.consumables[k][1] >= self.drops_array[i][p][j]:
                        print(self.consumables[k][0])
                        self.drops_array[i][p][j] = self.consumables[k][0]
                        break

    def getTerrain(self, player):
        return self.world_array[player.x][player.y]

    def getEnemy(self, player):
        return self.enemy_array[player.x][player.y]

    def clearEnemy(self, player):
        self.enemy_array[player.x][player.y] = ' '
        return

    def timeOfDay(self):
        self.time += 1
        if self.time == 12:
            print('Night has fallen, be prepared.')
            self.night = True

        if self.time == 24:
            print("Day has arrived.")
            self.night = False
            self.time = 0

    def probSum(self, array):
        sum = 0.0
        for i in range(len(array)):
            sum += array[i][1]
        for i in range(len(array)):
            if i == 0:
                array[i][1] = 100.0*array[i][1]/sum
            else:
                array[i][1] = (100.0*array[i][1]/sum) + array[i-1][1]
