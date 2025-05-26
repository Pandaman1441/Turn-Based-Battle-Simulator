from skill import Skill


class Fire_ball(Skill):
    def __init__(self):
        super().__init__(
            name = "Fire Ball",
            base_damage = 10,
            description = "test.",
            cost = 1
        )

    
    def use(self, user, target):
        import combat
        if combat.hit_chance(user, target):
            dmg = self._base_damage + (user.get_stat("mp")["current"] * 0.8)
            print(dmg)
            resistance = combat.magic_resistance(target)
            dmg = dmg - (dmg * resistance)
            print(dmg)
            combat.damage_target(dmg, target)
        else:
            print("you missed or they dodged")
        
        print(f"{self._name} has been used")

