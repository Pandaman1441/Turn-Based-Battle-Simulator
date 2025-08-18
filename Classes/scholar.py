from character import Character


# Deals magic damage mostly, support class. scales off mp, and some will power

class Scholar(Character):
    def __init__(self):
        name = "sch"
        gold = 3500
        base_stats = {
            "hp":       {"max": 500, "current": 500},
            "pp":       {"max": 10, "current": 10},
            "mp":       {"max": 25, "current": 25},
            "ag":       {"max": 5, "current": 5},
            "wp":       {"max": 10, "current": 10},
            "pr":       {"max": 8, "current": 8},
            "mr":       {"max": 8, "current": 8},
            "resource": {"max": 150, "current": 150},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": .8, "mp": 1.3, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/book_open.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

