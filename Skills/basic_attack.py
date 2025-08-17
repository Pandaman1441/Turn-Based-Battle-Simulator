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
            return(f"{self._name} has been used, {target.name} takes {result} damage.")

        else:
            return("you missed or they dodged")


