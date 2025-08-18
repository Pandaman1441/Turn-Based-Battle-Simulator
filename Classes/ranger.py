from character import Character


# mixed damage, scales off agility, pp, wp

class Ranger(Character):
    def __init__(self):
        name = "rang"
        gold = 3500
        base_stats = {
            "hp":       {"max": 360, "current": 360},
            "pp":       {"max": 15, "current": 15},
            "mp":       {"max": 6, "current": 6},
            "ag":       {"max": 20, "current": 20},
            "wp":       {"max": 10, "current": 10},
            "pr":       {"max": 9, "current": 9},
            "mr":       {"max": 7, "current": 7},
            "resource": {"max": 100, "current": 100},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1, "mp": 0, "ag": 1, "wp": .3, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile043.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

