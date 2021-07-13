from enemy import Orc, Goblin, Dragon, Vampire

enemies = {'orc' : Orc, 'goblin' : Goblin, 'dragon' : Dragon, 'vampire' : Vampire}

def combatLoop(type, player, world):
    enemy = enemies[type]()
    playerTurn = player.dexterity > enemy.dexterity
    while enemy.health > 0 and player.health > 0:
      playerTurn = combatOrder(playerTurn, player, enemy, type)

    if enemy.health <= 0:
      print('You won!')
      world.drops_array[player.x][player.y][0] = enemy.dropItem()
      return True

    elif player.health <= 0:
      print('You lost!')
      return False

def combatOrder(playerTurn, player, enemy, type):
    if playerTurn:

      if player.health > 0:
        print('Your Health : ' + str(player.health))
        print('Your Stamina : ' + str(player.stamina))

        attackStat, damage = player.attack()
        if attackStat >= enemy.armorClass:
          print('You hit.')
          enemy.health -= damage
          playerTurn = False

        elif attackStat == 0:
          playerTurn = False

        else:
          print('You miss.')
          playerTurn = False

      else:
        return playerTurn

    else:
      if enemy.health > 0:
        attackStat, damage = enemy.attack(player)
        if attackStat >= player.armorClass:
          print("The " + type + " hits.")
          player.health -= damage
          playerTurn = True

        elif attackStat == 0:
          playerTurn = True

        else:
          playerTurn = True
          print("The " + type + " misses.")

      else:
        return playerTurn

    return playerTurn
