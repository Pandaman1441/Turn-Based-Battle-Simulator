from character import Character


# deals physical damage, scales off agility, pp

class Thief(Character):
    def __init__(self):
        name = "thie"
        gold = 3500
        base_stats = {
            "hp":       {"max": 390, "current": 390},
            "pp":       {"max": 18, "current": 20},
            "mp":       {"max": 10, "current": 10},
            "ag":       {"max": 20, "current": 10},
            "wp":       {"max": 10, "current": 10},
            "pr":       {"max": 10, "current": 10},
            "mr":       {"max": 9, "current": 9},
            "resource": {"max": 80, "current": 80},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.7, "current": 1.7}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1.1, "mp": 0, "ag": 1.1, "wp": 0, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile058.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

