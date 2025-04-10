
import copy


# character template
class Character:

    def __init__(self):
        self._name = "Test"
        self._max_hp = 500
        self._max_resource = 300
        self._stats = { 
            "hp":       {"max": 500, "current": 500},        # health points
            "pp":       {"max": 1, "current": 20},          # physical power
            "mp":       {"max": 1, "current": 10},          # magical power
            "ag":       {"max": 1, "current": 10},          # dodge chance, inititive 
            "wp":       {"max": 1, "current": 1},          # willpower
            "pr":       {"max": 1, "current": 1},          # physical resist
            "mr":       {"max": 1, "current": 1},          # magical resist
            "resource": {"max": 300, "current": 300},         # mana or other type of resource like rage
        }
        self._accuracy = 1          # chance to hit
        self._crit_chance = 1
        self._crit_damage = 1.5
        self._actives = ["basic attack"]
        self._passives = []
        self._basic_attack_modifier = {
            "hp":       0 ,  
            "pp":       1,    
            "mp":       0,    
            "ag":       0.3,         
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
        value = sum(self._stats[stat]["current"] * mod for stat, mod in self._basic_attack_modifier.items())
        return value

    def get_all_stats(self):
        return copy.deepcopy(self._stats)

    def get_stat(self, stat):
        return self._stats[stat].copy()

    def set_current_stat(self, stat, value):
        self._stats[stat]["current"] = value

    def set_max_stat(self, stat, value):
        self._stats[stat]["max"] = value

    def get_accuracy(self):
        return self._accuracy
    
    def set_accuracy(self, value):
        self._accuracy = value
    
    def get_crit_chance(self):
        return self._crit_chance
    
    def set_crit_chance(self, value):
        self._crit_chance = value
    
    def get_crit_damage(self):
        return self._crit_damage
    
    def set_crit_damage(self, value):
        self._crit_damage = value

    def get_name(self):
        return self._name

    def get_actives(self):
        return self._actives.copy()
    
    def get_passives(self):
        return self._passives.copy()
    
    def add_active(self, skill=str):
        self._actives.append(skill)

    def add_passive(self, skill=str):
        self._passives.append(skill)

    def set_basic_attack_modifier(self, stat, value):
        self._basic_attack_modifier[stat] = value

# we can override a function to write it specifically for something or we can extend it using super().function()

# store active and passives skills in a list. Each skill can be an object

# the Skill abstract class can have the use() function to use the skill and on hit effects if needed 


# testing \/

p1 = Character()
stats = p1.get_all_stats()
# print(stats["hp"])
for key, value in stats.items():
    print(f"{key}: {value}")

ba = p1.get_basic_attack_modifier()
print(ba)