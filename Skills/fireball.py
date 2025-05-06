from skill import Skill


class Fire_ball(Skill):
    def __init__(self):
        self._name = "Skill"
        self._base_damage = 1
        self._description = "test."
        self._cost = 1


    def get_info(self):
        desc = f"Skill: {self._description} \nCost: {self._cost}"
        return desc
    
    def use(self, user, target):
        import combat
        if combat.hit_chance(user, target):
            dmg = self._base_damage + user.get_basic_attack_modifier()
            resistance = combat.physical_resistance(target)
            dmg *= resistance
            combat.damage_target(dmg, target)
        else:
            print("you missed or they dodged")
        
        print(f"{self._name} has been used")

