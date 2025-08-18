from abc import ABC, abstractmethod


class Skill(ABC):
    def __init__(self, name, base_damage, description, cost):
        self._name = name
        self._base_damage = base_damage
        self._description = description
        self._cost = cost

    def get_info(self):
        desc = f"{self._name}: {self._description} \nCost: {self._cost}"
        return desc
    
    @abstractmethod
    def use(self, user, target):
        pass

    #@abstractmethod
    def targetting(self, user):
        pass
    # should call use instead 
 

    # skills are loaded by string in the character object, we don't keep a reference of the skill objects 
    # and just call them by matching string names then immediatly use them. they are then garbage collected afterwards