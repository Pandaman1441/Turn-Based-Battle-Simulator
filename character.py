
from enemy import Enemy


# character template
class Character:

    def __init__(self):
        self._name = "Name"
        self._stats = { 
            "hp":       500,        # health points
            "pp":       1,          # physical power
            "mp":       1,          # magical power
            "ag":       1,          # dodge chance, inititive 
            "wp":       1,          # willpower
            "pr":       1,          # physical resist
            "mr":       1,          # magical resist
            "resource": 300         # mana or other type of resource like rage
        }
        self._accuracy = 1          # chance to hit
        self._crit_chance = 1
        self._crit_damage = 1.5
        self._actives = []
        self._passives = []
        self._basic_attack_modifier = {
            "hp":       0 ,  
            "pp":       1,    
            "mp":       0,    
            "ag":       0,         
            "wp":       0,  
            "pr":       0,    
            "mr":       0,    
            "resource": 0  
        }

    def __str__(self):
        pass

    def intro(self):
        pass


    def get_basic_attack_modifier(self):
        value = sum(self._stats[stat] * mod for stat, mod in self._basic_attack_modifier.items())
        return value

    def get_all_stats(self):
        return self._stats.copy()

    def get_stat(self, stat):
        return self._stats[stat]

    def set_stat(self, stat, value):
        self._stats[stat] = value



# we can override a function to write it specifically for something or we can extend it using super().function()

# store active and passives skills in a list. Each skill can be an object

# the Skill abstract class can have the use() function to use the skill and on hit effects if needed 


# testing \/

p1 = Character()
stats = p1.get_all_stats()
print(stats["hp"])
for key, value in stats.items():
    print(f"{key}: {value}")

ba = p1.get_basic_attack_modifier()
print(ba)