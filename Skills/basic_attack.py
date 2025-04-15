from skill import Skill


class Basic_Attack(Skill):
    def __init__(self):
        self._name = "basic attack"
        self._base_damage = 1
        self._description = "test."
        self._cost = 1
        print(f"{self._name} have been initialized")

    def get_info(self):
        desc = f"Skill: {self._description} \nCost: {self._cost}"
        return desc
    
    def use(self, user, target):
        import combat
        if combat.hit_chance(user, target):
            dmg = self._base_damage + user.get_basic_attack_modifier()
            resistance = combat.physical_resistance(target)
            print(f"pre damage: {dmg}")
            dmg *= resistance
            print(f"post damgae: {dmg}")
            combat.damage_target(dmg, target)
        else:
            pass
        
        print(f"{self._name} has been used")

