from character import Character


# deals mixed damage, scales off pp, wp, frontline support

class Cleric(Character):
    def __init__(self):
        name = "cler"
        gold = 3500
        base_stats = {
            "hp":       {"max": 440, "current": 440},
            "pp":       {"max": 25, "current": 25},
            "mp":       {"max": 7, "current": 7},
            "ag":       {"max": 5, "current": 5},
            "wp":       {"max": 15, "current": 15},
            "pr":       {"max": 13, "current": 13},
            "mr":       {"max": 13, "current": 13},
            "resource": {"max": 100, "current": 100},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.7, "current": 1.7}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": 0, "pp": 1, "mp": 0, "ag": 0, "wp": .8, "pr": 0, "mr": 0, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile032.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

