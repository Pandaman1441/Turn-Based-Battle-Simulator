from character import Character


# deals most magic damage with some physical damage, scales off mostly mp, and some agility, pp

class Bladeslinger(Character):
    def __init__(self):
        name = "wiz"
        gold = 3500
        base_stats = {
            "hp":       {"max": 380, "current": 380},
            "pp":       {"max": 18, "current": 18},
            "mp":       {"max": 15, "current": 15},
            "ag":       {"max": 11, "current": 11},
            "wp":       {"max": 8, "current": 8},
            "pr":       {"max": 9, "current": 9},
            "mr":       {"max": 9, "current": 9},
            "resource": {"max": 120, "current": 120},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1.2, "mp": 1.2, "ag": 0, "wp": 0, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile009.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)


    