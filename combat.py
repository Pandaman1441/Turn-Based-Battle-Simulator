
import math
import random


# This is where we can do damage calculations, apply crits, 

# Resistances have dimishing returns for how much they reduce damage by

# Dodge chance is based on agility, capped at 60% chance to dodge



def dodge_chance(ag):
    n = 80
    value = (ag * .70) / (ag+n)
    print(f"dodge chance: {value}")
    return value

def magic_resistance(entity):
    r = entity.get_stat("mr")
    r = r["current"]
    n = 90
    value = (r * 1) / (r+n)
    # print(f"magical resistance: {value}")
    return value

def physical_resistance(entity):
    r = entity.get_stat("pr")
    r = r["current"]
    n = 90
    value = (r * 1) / (r+n)
    # print(f"physical resistance: {value}")
    return value

def hit_chance(user, target):
    a = user.get_stat("accuracy")["current"]
    d = dodge_chance(target.get_stat("ag")["current"]) * 100
    d = math.floor(d)
    hc = a - d
    print(f"accuracy: {a} dodge chance: {d}")
    hc = max(5, min(hc, 95))
    roll = random.randint(0,100)
    print(f"roll: {roll}, beat hit chance: {hc}")
    if roll <= hc:
        # print("hit landed. Calculating damage")
        return True
    else:
        # print("you missed")
        return False

def damage_target(user, dmg, target):
    stat = target.get_stat("hp")
    dmg = math.ceil(dmg)
    # crit calc
    roll = random.randint(1,100)
    if roll <= user.get_stat("crit_chance")["current"]:
        print("critical hit!")
        dmg = (user.get_stat("crit_dmg")["current"]) * dmg

    target_hp = stat["current"] - dmg
    target_hp = max(target_hp, 0)
    target.set_current_stat("hp", target_hp)

def heal_target(value, target):
    stat = target.get_stat("hp")
    value = math.ceil(value)
    target_hp = stat["current"] + value
    target_hp = min(target_hp, stat["max"])
    target.set_current_stat("hp", target_hp)


def roll_inititve(entity):
    i = (entity.get_stat("ag") * 0.6) + random.randint(0,100)
    entity.inititive = i
    
