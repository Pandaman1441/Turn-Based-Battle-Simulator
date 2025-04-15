
import copy
from Skill_Loader import load_skills

# character template
class Character:

    def __init__(self):
        self._name = "Test"
        self._level = 1
        self._ex = 0
        self._stats = { 
            "hp":       {"max": 500, "current": 500},        # health points
            "pp":       {"max": 20, "current": 20},          # physical power
            "mp":       {"max": 10, "current": 10},          # magical power
            "ag":       {"max": 10, "current": 10},          # dodge chance, inititive 
            "wp":       {"max": 10, "current": 10},          # willpower
            "pr":       {"max": 10, "current": 10},          # physical resist
            "mr":       {"max": 10, "current": 10},          # magical resist
            "resource": {"max": 300, "current": 300},         # mana or other type of resource like rage
        }
        self._accuracy = 80          # chance to hit
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
        self._loaded_actives = load_skills(self._actives)
        self._loaded_passives = load_skills(self._passives)


        # load skills into a list of objects, anytime we add a new skill we just 

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
        self._loaded_actives = load_skills(self._actives)

    def add_passive(self, skill=str):
        self._passives.append(skill)
        self._loaded_passives = load_skills(self._passives)


    def set_basic_attack_modifier(self, stat, value):
        self._basic_attack_modifier[stat] = value

    def use_skill(self, skill_name, target):
        skill = next((s for s in self._loaded_actives if s.name == skill_name), None)
        if skill:
            skill.use(user=self, target=target)
        else:
            print(f"{self._name} does not know the skill '{skill_name}'.")

    def get_loaded_actives(self):
        return self._loaded_actives.copy()

    def get_loaded_passives(self):
        return self._loaded_passives.copy() 

# we can override a function to write it specifically for something or we can extend it using super().function()

# store active and passives skills in a list. Each skill can be an object

# the Skill abstract class can have the use() function to use the skill and on hit effects if needed 


# testing \/

# from Skills import skill_registry
p1 = Character()
p2 = Character()
skills = p1.get_actives()

l = p1.get_loaded_actives()
r = l[0]
r.use(p1, p2)