from character import Character


# deals mixed but leans towards physical damage, scales off pp and some wp

class Mercenary(Character):
    def __init__(self):
        name = "merc"
        gold = 3500
        base_stats = {
            "hp":       {"max": 420, "current": 420},
            "pp":       {"max": 25, "current": 25},
            "mp":       {"max": 8, "current": 8},
            "ag":       {"max": 12, "current": 12},
            "wp":       {"max": 12, "current": 12},
            "pr":       {"max": 12, "current": 12},
            "mr":       {"max": 8, "current": 8},
            "resource": {"max": 80, "current": 80},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1.3, "mp": 0, "ag": .3, "wp": .7, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile008.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)
