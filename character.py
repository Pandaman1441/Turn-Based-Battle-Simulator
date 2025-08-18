import copy
import math
from Skill_Loader import load_skills
from item_loader import load_items

# character template
class Character:
    def __init__(self, name: str, base_stats: dict, attack_mod: dict, gold: int = 0, actives: list[str] = None, passives: list[str] = None,  inventory: list[str] = None, icon: str = None):
        self.__name = name
        self.__level = 1
        self.__ex = 0
        self.__inititive = 0
        self.__gold = gold
        self.__base_stats = copy.deepcopy(base_stats)
        self.__stats = copy.deepcopy(base_stats)
        self.__actives = actives if actives else []
        self.__passives = passives if passives else []
        self.__inventory = inventory if inventory else []
        self.__basic_attack_modifier = copy.deepcopy(attack_mod)
        self.__loaded_actives = load_skills(self.__actives)
        self.__loaded_passives = load_skills(self.__passives)
        self.__loaded_inventory = load_items(self.__inventory)
        self.__basic_attack = load_skills(["basic attack"])
        self.__icon = icon or "Assets/item_icons/placeholder.png"

 
    def __str__(self):
        pass

    def intro(self):
        pass

    def basic_attack(self, target):
        result = self.__basic_attack[0].use(self, target)
        return result

    def get_basic_attack_modifier(self):
        value = sum(self.__stats[stat]["current"] * mod for stat, mod in self.__basic_attack_modifier.items())
        return value
    
    def update_stats(self):
        old_stats = copy.deepcopy(self.__stats)
        self.__stats = copy.deepcopy(self.__base_stats)
        for item in self.__loaded_inventory:
            i_stats = item.get_stats()
            for stat, mod in i_stats.items():
                self.__stats[stat]["max"] += mod 
        for stat in self.__stats:
            percentage = old_stats[stat]["current"] / old_stats[stat]["max"]
            self.__stats[stat]["current"] = math.ceil(self.__stats[stat]["max"] * percentage)

    @property
    def stats(self):
        return copy.deepcopy(self.__stats)

    def get_stat(self, stat):                       #.get_stat("stat")["current"]
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
        if len(self.__inventory) < 10:
            self.__inventory.append(item)
            self.__loaded_inventory = load_items(self.__inventory)
            return True
        else:
            return False
    
    def get_inventory(self):
        return self.__inventory.copy()
    
    def get_loaded_inventory(self):
        return self.__loaded_inventory.copy()
    
    @property
    def gold(self):
        return self.__gold
    
    
    def add_gold(self, value):
        self.__gold += value

    def take_gold(self, value):
        if value > self.__gold:
            return False            # flag if gold was taken successfully
        else:
            self.__gold -= value
            return True

    @property
    def icon(self):
        return self.__icon
# we can override a function to write it specifically for something or we can extend it using super().function()

# store active and passives skills in a list. Each skill can be an object

# the Skill abstract class can have the use() function to use the skill and on hit effects if needed 


# testing \/

# from Skills import skill_registry
# p1 = Character(name = "art",
#         gold = 3500,
#         base_stats = {
#             "hp":       {"max": 500, "current": 500},
#             "pp":       {"max": 20, "current": 20},
#             "mp":       {"max": 10, "current": 10},
#             "ag":       {"max": 10, "current": 10},
#             "wp":       {"max": 10, "current": 10},
#             "pr":       {"max": 10, "current": 10},
#             "mr":       {"max": 10, "current": 10},
#             "resource": {"max": 300, "current": 300},
#             "accuracy": {"max": 80, "current": 80},
#             "crit_chance": {"max": 0, "current": 0},
#             "crit_dmg": {"max": 1.5, "current": 1.5}
#         },
#         actives = ["basic attack", "fireball"],
#         passives = [],
#         attack_mod = {"hp": 0, "pp": 1, "mp": 0, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": 0},
#         inventory = ["Buckler", "Razor Fang", "Ironclaw", "Heartstone"],
#         icon = "Assests/class_icons/R.png")
# p2 = Character(name = "art",
#         gold = 3500,
#         base_stats = {
#             "hp":       {"max": 500, "current": 500},
#             "pp":       {"max": 20, "current": 20},
#             "mp":       {"max": 10, "current": 10},
#             "ag":       {"max": 10, "current": 10},
#             "wp":       {"max": 10, "current": 10},
#             "pr":       {"max": 40, "current": 40},
#             "mr":       {"max": 10, "current": 10},
#             "resource": {"max": 300, "current": 300},
#             "accuracy": {"max": 80, "current": 80},
#             "crit_chance": {"max": 0, "current": 0},
#             "crit_dmg": {"max": 1.5, "current": 1.5}
#         },
#         actives = ["basic attack"],
#         passives = [],
#         attack_mod = {"hp": 0, "pp": 1, "mp": 0, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": 0},
#         inventory = ["Buckler", "Razor Fang", "Ironclaw", "Heartstone"],
#         icon = "Assests/class_icons/R.png")
# skills = p1.get_actives()

# l = p1.get_loaded_actives()
# r = l[1]
# r.use(p1, p2)

# hp = p2.get_stat("hp")
# print(hp["current"])