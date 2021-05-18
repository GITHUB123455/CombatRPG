from enemy import Orc, Goblin, Dragon, Vampire

enemies = {'orc' : Orc, 'goblin' : Goblin, 'dragon' : Dragon, 'vampire' : Vampire}

def combatLoop(type, player, world):
    enemy = enemies[type]()
    playerDex = player.dexterity
    while enemy.health > 0 and player.health > 0:
      playerDex = combatOrder(playerDex, player, enemy, type)

    if enemy.health <= 0:
      print('You won!')
      world.drops_array[player.x][player.y][0] = enemy.dropItem()
      return True

    elif player.health <= 0:
      print('You lost.')
      return False

def combatOrder(playerDex, player, enemy, type):
    if playerDex >= enemy.dexterity:

      if player.health > 0:
        print('Your Health : ' + str(player.health))
        print('Your Stamina : ' + str(player.stamina))

        attackStat, damage = player.attack()
        if attackStat >= enemy.armorClass:
          print('You hit.')
          enemy.health -= damage
          playerDex -= 1

        elif attackStat == 0:
          playerDex -= 1

        else:
          print('You miss.')
          playerDex -= 1

      else:
        return playerDex

    if enemy.dexterity >= playerDex:
      if enemy.health > 0:
        attackStat, damage = enemy.attack(player)
        if attackStat >= player.armorClass:
          print("The " + type + " hits.")
          player.health -= damage
          enemy.dexterity -= 1

        elif attackStat == 0:
          enemy.dexterity -= 1

        else:
          enemy.dexterity -= 1
          print("The " + type + " misses.")

      else:
        return playerDex

    return playerDex
