from character import Character


# deals mixed damage, scales off resists, hp, wp, pp

class Paladin(Character):
    def __init__(self):
        name = "pal"
        gold = 3500
        base_stats = {
            "hp":       {"max": 460, "current": 460},
            "pp":       {"max": 18, "current": 18},
            "mp":       {"max": 5, "current": 5},
            "ag":       {"max": 5, "current": 5},
            "wp":       {"max": 14, "current": 14},
            "pr":       {"max": 17, "current": 17},
            "mr":       {"max": 15, "current": 15},
            "resource": {"max": 80, "current": 80},
            "accuracy": {"max": 80, "current": 80},
            "crit_chance": {"max": 0, "current": 0},
            "crit_dmg": {"max": 1.5, "current": 1.5}
        }
        actives = []
        passives = []
        basic_attack_modifier = {"hp": .02, "pp": .8, "mp": 0, "ag": 0, "wp": .5, "pr": .3, "mr": .3, "resource": 0}
        inventory = []
        icon_path = "Assets/class_icons/tile036.png"
        super().__init__(name, base_stats, basic_attack_modifier, gold, actives, passives, inventory, icon_path)

#  9.2 +14.4 + 7 + 5.1 + 4.3