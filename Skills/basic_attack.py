from skill import Skill


class Basic_Attack(Skill):
    def __init__(self):
        super().__init__(
            name = "Basic Attack",
            base_damage = 0,
            description = "test.",
            cost = 0
        )

    
    def use(self, user, target):
        import combat
        if combat.hit_chance(user, target):
            dmg = user.get_basic_attack_modifier()
            # print(dmg)
            resistance = combat.physical_resistance(target)
            dmg = dmg - (dmg * resistance)
            # print(dmg)
            result = combat.damage_target(user, dmg, target)
            print(f"{user.name} uses {self._name} on {target.name} for {result} points of damage.")
            return(f"{self._name} has been used, {target.name} takes {result} damage.")

        else:
            print("you missed or they dodged")
            return("you missed or they dodged")


