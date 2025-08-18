from character import Character


# deals mostly physical damage, scales off of health, physical power. abilites could scale off willpower

class Barbarian(Character):
    def __init__(self):
        name = "barb"
        gold = 3500
        base_stats = {
            "hp":       {"max": 480, "current": 480},
            "pp":       {"max": 20, "current": 20},
            "mp":       {"max": 5, "current": 5},
            "ag":       {"max": 5, "current": 5},
            "wp":       {"max": 8, "current": 8},
            "pr":       {"max": 9, "current": 9},
            "mr":       {"max": 6, "current": 6},
            "resource": {"max": 80, "current": 80},
            "accuracy": {"max": 75, "current": 75},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": .06, "pp": 1.2, "mp": 0, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile026.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)


