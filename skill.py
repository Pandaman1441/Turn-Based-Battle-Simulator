

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


    # skills are loaded by string in the character object, we don't keep a reference of the skill objects 
    # and just call them by matching string names then immediatly use them. they are then garbage collected afterwards