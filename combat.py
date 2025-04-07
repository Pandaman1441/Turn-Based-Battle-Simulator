
import math
import random
from character import Character


# This is where we can do damage calculations, apply crits, 

# Resistances have dimishing returns for how much they reduce damage by

# Dodge chance is based on agility, capped at 60% chance to dodge



def dodge_chance(entity=Character):
    a = entity.get_stat("ag")
    a = a["current"]
    n = 70
    value = (a * .75) / (a+n)

    return value

def magic_resistance(entity=Character):
    r = Character.get_stat("mr")
    r = r["current"]
    n = 90
    value = (r * 1) / (r+n)
    return value

def physical_resistance(entity=Character):
    r = Character.get_stat("pr")
    r = r["current"]
    n = 90
    value = (r * 1) / (r+n)
    return value

def hit_chance(user=Character, target=Character):
    a = user.get_accuracy()
    d = dodge_chance(target.get_stat("ag")["current"]) * 100
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

def damage_target(dmg, target=Character):
    stat = target.get_stat("hp")
    print(f"{target.get_name} HP: {stat}")
    target_hp = stat["current"] - dmg
    print(f"new value should be: {target_hp}")
    target_hp = max(target_hp, 0)
    print(f"new value should be: {target_hp}")
    target.set_current_stat("hp", target_hp)

def heal_target(value, target=Character):
    stat = target.get_stat("hp")
    target_hp = stat["current"] + value
    target_hp = min(target_hp, stat["max"])
    target.set_current_stat("hp", target_hp)



# print(dodge_chance())
# print(physical_resistance())
# hit_chance()



# This was testing the copies making sure values aren't changed mid process
# p1 = Character()
# p2 = Character()

# p1_stats = p1.get_all_stats()
# p2_stats = p2.get_all_stats()

# print("\np2: ")
# for key, value in p2_stats.items():
#     print(f"{key}: {value}")

# print("\ndealing 10 damage to p2.\n")

# damage_target(10, p2)
# print("\np2: ")
# value = p2.get_stat("hp")
# print(value)