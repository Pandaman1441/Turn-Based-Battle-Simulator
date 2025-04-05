from character import Character

# deals mostly physical damage, scales off of health, physical power. abilites could scale off willpower

class Barbarian(Character):
    def __init__(self):
        self.name = "bar"
        self.hp = 1
        self.ad = 1
        self.ap = 1
        self.critChance = 1
    
    def __str__(self):
        pass

    def intro(self):
        pass

    def display(self):
        print(self.name + "\n")
        print("===================")
        print("Health Points: " + str(self.hp))
        print("Attack Power: " + str(self.ad))
        print("Ability Power: " + str(self.ap))
        print("Critical Chance: " + str(self.critChance))

    def basic_attack(self, target):
        pass