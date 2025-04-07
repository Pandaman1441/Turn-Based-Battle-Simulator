from skill import Skill
from character import Character
import combat


class Basic_Attack(Skill):
    def init(self):
        self._name = "Skill"
        self._base_damage = 1
        self._description = "test."
        self._cost = 1

    def get_info(self):
        desc = f"Skill: {self._description} \nCost: {self._cost}"
        return desc
    
    def use(self, user=Character, target=Character):
        if combat.hit_chance(user, target):
            dmg = self._base_damage + user.get_basic_attack_modifier
            resistance = combat.physical_resistance(target)
            dmg *= resistance
            combat.damage_target(dmg, target)
        else:
            print("you missed or they dodged")

