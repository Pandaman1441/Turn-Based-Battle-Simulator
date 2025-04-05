
import math
import random


# This is where we can do damage calculations, apply crits, 

# Resistances have dimishing returns for how much they reduce damage by

# Dodge chance is based on agility, capped at 60% chance to dodge



def dodge_chance():
    a = 30
    n = 70
    value = (a * .75) / (a+n)

    return value



def resistance():
    r = 300
    n = 90
    value = (r * 1) / (r+n)
    return value



def hit_chance():
    a = 80
    d = dodge_chance() * 100
    d = math.ceil(d)

    hc = a - d
    hc = max(5, min(hc, 95))
    print("hit chance: " + str(hc))
    roll = random.randint(0,100)
    print("roll: " + str(roll))

    if roll <= hc:
        print("hit landed. Calculating damage")
    else:
        print("you missed")



# print(dodge_chance())
# print(resistance())
hit_chance()