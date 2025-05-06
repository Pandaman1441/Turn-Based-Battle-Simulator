
import copy
import math
from Skill_Loader import load_skills
from item_loader import load_items

# character template
class Character:

    def __init__(self):
        self.__name = "Test"
        self.__level = 1
        self.__ex = 0
        self.__base_stats = {
            "hp":       500,  
            "pp":       20,    
            "mp":       10,    
            "ag":       10,         
            "wp":       10,  
            "pr":       10,    
            "mr":       10,    
            "resource": 300,
            "accuracy": 80,
            "crit_change": 1,
            "crit_dmg": 1.5
        }
        self.__stats = { 
            "hp":       {"max": 500, "current": 500},        # health points
            "pp":       {"max": 20, "current": 20},          # physical power
            "mp":       {"max": 10, "current": 10},          # magical power
            "ag":       {"max": 10, "current": 10},          # dodge chance, inititive 
            "wp":       {"max": 10, "current": 10},          # willpower
            "pr":       {"max": 10, "current": 10},          # physical resist
            "mr":       {"max": 10, "current": 10},          # magical resist
            "resource": {"max": 300, "current": 300},        # mana or other type of resource like rage
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 1, "current": 1},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        self.__actives = ["basic attack"]
        self.__passives = []
        self.__inventory = []
        self.__basic_attack_modifier = {
            "hp":       0 ,  
            "pp":       1,    
            "mp":       0,    
            "ag":       0.3,         
            "wp":       0,  
            "pr":       0,    
            "mr":       0,    
            "resource": 0  
        }
        self.__loaded_actives = load_skills(self.__actives)
        self.__loaded_passives = load_skills(self.__passives)
        self.__loaded_inventory = load_items(self.__inventory)


    def __str__(self):
        pass

    def intro(self):
        pass


    def get_basic_attack_modifier(self):
        value = sum(self.__stats[stat]["current"] * mod for stat, mod in self.__basic_attack_modifier.items())
        return value
    
    def update_stats(self):
        old_stats = copy.deepcopy(self.__stats)
        self.__stats = copy.deepcopy(self.__base_stats)
        for item in self.__inventory:
            i_stats = item.get_stats()
            for stat, mod in i_stats.items():
                self.__stats[stat]["max"] += mod 
        for stat in self.__stats:
            percentage = old_stats[stat]["current"] / old_stats[stat]["max"]
            self.__stats[stat]["current"] = math.ceil(self.__stats[stat]["max"] * percentage)


    @property
    def stats(self):
        return copy.deepcopy(self.__stats)

    def get_stat(self, stat):
        return self.__stats[stat].copy()

    def set_current_stat(self, stat, value):
        self.__stats[stat]["current"] = value

    def set_max_stat(self, stat, value):
        self.__stats[stat]["max"] = value

    @property
    def name(self):
        return self.__name

    def get_actives(self):
        return self.__actives.copy()
    
    def get_passives(self):
        return self.__passives.copy()
    
    def add_active(self, skill=str):
        self.__actives.append(skill)
        self.__loaded_actives = load_skills(self.__actives)

    def add_passive(self, skill=str):
        self.__passives.append(skill)
        self.__loaded_passives = load_skills(self.__passives)

    def set_basic_attack_modifier(self, stat, value):
        self.__basic_attack_modifier[stat] = value

    def use_skill(self, skill_name, target):
        skill = next((s for s in self.__loaded_actives if s.name == skill_name), None)
        if skill:
            skill.use(user=self, target=target)
        else:
            print(f"{self.__name} does not know the skill '{skill_name}'.")

    def get_loaded_actives(self):
        return self.__loaded_actives.copy()

    def get_loaded_passives(self):
        return self.__loaded_passives.copy() 
    
    def add_item(self, item=str):
        self.__inventory.append(item)
        self.__loaded_inventory = load_items(self.__inventory)
    
    def get_inventory(self):
        return self.__inventory.copy()
    
    def get_loaded_inventory(self):
        return self.__loaded_inventory.copy()

# we can override a function to write it specifically for something or we can extend it using super().function()

# store active and passives skills in a list. Each skill can be an object

# the Skill abstract class can have the use() function to use the skill and on hit effects if needed 


# testing \/

# from Skills import skill_registry
# p1 = Character()
# p2 = Character()
# skills = p1.get_actives()

# l = p1.get_loaded_actives()
# r = l[0]
# r.use(p1, p2)

# hp = p2.get_stat("hp")
# print(hp["current"])