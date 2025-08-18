from character import Character


# deals physical or some true damage, scales off pp, wp, and agility

class Monk(Character):
    def __init__(self):
        name = "monk"
        gold = 3500
        base_stats = {
            "hp":       {"max": 400, "current": 400},
            "pp":       {"max": 22, "current": 22},
            "mp":       {"max": 5, "current": 5},
            "ag":       {"max": 17, "current": 17},
            "wp":       {"max": 17, "current": 17},
            "pr":       {"max": 8, "current": 8},
            "mr":       {"max": 8, "current": 8},
            "resource": {"max": 100, "current": 100},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1, "mp": 0, "ag": .5, "wp": .5, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/fist.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

