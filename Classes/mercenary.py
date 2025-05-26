from character import Character


# deals mixed but leans towards physical damage, scales off pp and some wp

class Mercenary(Character):
    def __init__(self):
        name = "merc"
        gold = 3500
        base_stats = {
            "hp":       {"max": 500, "current": 500},
            "pp":       {"max": 20, "current": 20},
            "mp":       {"max": 10, "current": 10},
            "ag":       {"max": 10, "current": 10},
            "wp":       {"max": 10, "current": 10},
            "pr":       {"max": 10, "current": 10},
            "mr":       {"max": 10, "current": 10},
            "resource": {"max": 300, "current": 300},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = ["basic attack"]
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1, "mp": 0, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": 0}
        inventory = ["Buckler", "Razor Fang", "Ironclaw", "Heartstone"]
        icon_path = "Assests/class_icons/tile008.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)
