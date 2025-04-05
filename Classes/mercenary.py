from character import Character

# deals mixed but leans towards physical damage, scales off pp and some wp

class Mercenary(Character):
    def __init__(self):
        self.name = "figh"
        self.hp = 500              
        self.pp = 65               
        self.mp = 10                  
        self.agility = 1            
        self.wp = 1                 
        self.pr = 1                
        self.mr = 1                 
        self.resource = 300         
        self.accuracy = 1           
        self.crit_chance = 1
        self.crit_damage = 1.5
        self.active = []
        self.passive = []

    def __str__(self):
        pass

    def intro(self):
        pass

    def display(self):
        print(self.name + "\n")
        print("===================")
        print("Health Points: " + str(self.hp))
        print("Physical Power: " + str(self.pp))
        print("Magical Power: " + str(self.mp))
        print("Critical Chance: " + str(self.crit_chance))

