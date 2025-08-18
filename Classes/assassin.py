from character import Character


# PD, scales off crit chance, pp and some agility

class Assassin(Character):
    def __init__(self):
        name = "ass"
        gold = 3500
        base_stats = {
            "hp":       {"max": 380, "current": 380},
            "pp":       {"max": 18, "current": 18},
            "mp":       {"max": 10, "current": 10},
            "ag":       {"max": 20, "current": 20},
            "wp":       {"max": 8, "current": 8},
            "pr":       {"max": 11, "current": 11},
            "mr":       {"max": 9, "current": 9},
            "resource": {"max": 80, "current": 80},
            "accuracy": {"max": 85, "current": 85},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.6, "current": 1.6}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1.3, "mp": 0, "ag": .9, "wp": 0, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile000.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)


