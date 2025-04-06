
import math
import random
from character import Character


# This is where we can do damage calculations, apply crits, 

# Resistances have dimishing returns for how much they reduce damage by

# Dodge chance is based on agility, capped at 60% chance to dodge



def dodge_chance(entity=Character):
    a = entity.get_stat("ag")
    n = 70
    value = (a * .75) / (a+n)

    return value

def magic_resistance(entity=Character):
    r = Character.get_stat("mr")
    n = 90
    value = (r * 1) / (r+n)
    return value

def physical_resistance(entity=Character):
    r = Character.get_stat("pr")
    n = 90
    value = (r * 1) / (r+n)
    return value

def hit_chance(user=Character, target=Character):
    a = user.get_accuracy()
    d = dodge_chance(target.get_stat("ag")) * 100
    d = math.ceil(d)

    hc = a - d
    hc = max(5, min(hc, 95))
    print("hit chance: " + str(hc))
    roll = random.randint(0,100)
    print("roll: " + str(roll))

    if roll <= hc:
        print("hit landed. Calculating damage")
        return True
    else:
        print("you missed")
        return False

def deal_damage(dmg, target=Character):
    target_hp = target.get_stat("hp")
    target_hp -= dmg
    target_hp = max(target_hp, 0)
    target.set_stat("hp", target_hp)



# print(dodge_chance())
# print(physical_resistance())
# hit_chance()