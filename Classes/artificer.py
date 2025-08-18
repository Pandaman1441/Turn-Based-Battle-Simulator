from character import Character


# deals mixed damge, scales on mp, and some resource. use more resource to empower abilities

class Artificer(Character):
    def __init__(self):
        name = "art"
        gold = 3500
        base_stats = {
            "hp":       {"max": 360, "current": 360},
            "pp":       {"max": 15, "current": 15},
            "mp":       {"max": 18, "current": 18},
            "ag":       {"max": 5, "current": 5},
            "wp":       {"max": 8, "current": 8},
            "pr":       {"max": 8, "current": 8},
            "mr":       {"max": 10, "current": 10},
            "resource": {"max": 150, "current": 150},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.6, "current": 1.6}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": .8, "mp": .2, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": .17}
        inventory = []
        icon_path = "Assets/class_icons/R.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

# 42 base dmg

