from enemy import Orc, Goblin, Dragon, Vampire
import random
enemies = {'orc' : Orc, 'goblin' : Goblin, 'dragon' : Dragon, 'vampire' : Vampire}

def combatLoop(type, player, world):
    enemy = enemies[type]()
    PlayerTurn = player.dexterity > enemy.dexterity
    while enemy.health > 0 and player.health > 0:
        PlayerTurn = combatOrder(PlayerTurn, player, enemy, type)

        if enemy.health <= 0:
            print('You won!')
            world.drops_array[player.x][player.y][0] = enemy.dropItem()
            return 1

        elif PlayerTurn == -1:
            return -1
        elif player.health <= 0:
            print('You lost.')
            return 0

def combatOrder(PlayerTurn, player, enemy, type):
    if PlayerTurn == 1:
        PlayerTurn = 0
        if player.health > 0:
            print('Your Health : ' + str(player.health))
            print('Your Stamina : ' + str(player.stamina))

            attackStat, damage = player.attack()
            if attackStat >= enemy.armorClass:
                print('You hit.')
                enemy.health -= damage

            elif attackStat == 0:
                return PlayerTurn

            elif attackStat == -1:
                PlayerEscape = random.randrange(0,20) + player.dexterity
                EnemyCatch = random.randrange(0,20) + enemy.dexterity
                if PlayerEscape > EnemyCatch:
                    print('You barely managed to escape!')
                    PlayerTurn = -1
                    return PlayerTurn
                else:
                    print('The enemy managed to catch up!')
                    return PlayerTurn

            else:
                print('You miss.')


        else:
            return PlayerTurn

    elif PlayerTurn == 0:
        PlayerTurn = 1
        if enemy.health > 0:
            attackStat, damage = enemy.attack(player)
            if attackStat >= player.armorClass:
                print("The " + type + " hits.")
                player.health -= damage
                player.inventory.equippedArmour.durability -= int(damage * .166)
                if player.inventory.equippedArmour.durability <= 0:
                    player.inventory.equippedArmour = None


                elif attackStat == 0:
                    return PlayerTurn


                else:
                    print("The " + type + " misses.")

            else:
                return PlayerTurn

    return PlayerTurn
