

class Skill():
    def init(self):
        self._name = "Skill"
        self._base_damage = 1
        self._description = "test."
        self._cost = 1

    def get_info(self):
        desc = f"Skill: {self._description} \nCost: {self._cost}"
        return desc
    
    def use(self, user, target):
        pass