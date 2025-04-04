



# character template
class Character:

    def __init__(self):
        self.name = "Name"
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


# we can override a function to write it specifically for something or we can extend it using super().function()

# store active and passives skills in a list. Each skill can be an object

# the Skill abstract class can have the use() function to use the skill and on hit effects if needed 