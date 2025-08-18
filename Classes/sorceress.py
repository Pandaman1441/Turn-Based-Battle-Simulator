from character import Character


# deals magic damage, scales off wp, resource, can burn more resource for stronger effects

class Sorceress(Character):
    def __init__(self):
        name = "sorc"
        gold = 3500
        base_stats = {
            "hp":       {"max": 360, "current": 360},
            "pp":       {"max": 8, "current": 8},
            "mp":       {"max": 10, "current": 10},
            "ag":       {"max": 8, "current": 8},
            "wp":       {"max": 25, "current": 25},
            "pr":       {"max": 7, "current": 7},
            "mr":       {"max": 7, "current": 7},
            "resource": {"max": 150, "current": 150},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": .8, "mp": 0, "ag": 0, "wp": 1.2, "pr": 0, "mr": 0, "resource": 0.08}
        inventory = []
        icon_path = "Assets/class_icons/tile063.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

