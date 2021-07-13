from player import Player
from world import WorldSpace
from combat import combatLoop

scale = int(input("Input your desired world scale. "))

player = Player(int(scale/2), int(scale/2), scale)
world = WorldSpace(scale)
world.worldGen()
world.terrainGen()
world.enemyGeneration(player)
world.consumablesGen()


while True:
    if player.infected and player.infectedDuration == 0:
        print("You have succumbed to vampiritis. Game over.")
        break

    if player.counter > 10:
        world.enemyGeneration(player)
        player.counter = 0
        print("The Blood Moon rises, the enemies have gathered their strength again.")

    w, c = player.getDrops(world)
    if w != ' ':
      player.pickupDrops(world, 0)
    if c != ' ':
      player.pickupDrops(world, 1)

    if world.getEnemy(player) == ' ':
        terrain = world.getTerrain(player)
        print('You are in the ' + terrain + '.')
        player.decision()
    else:
        enemy = world.getEnemy(player)
        terrain = world.getTerrain(player)
        print('You are in the ' + terrain + '.')
        if enemy == "vampire" and world.night == False:
            player.decision()
        print('You see a(n) ' + enemy + '.')
        victory = combatLoop(enemy, player, world)
        if victory == True:
            world.clearEnemy(player)
            player.pickupDrops(world, 1)
            player.decision()
        if victory == False:
            print('Game Over')
            break
