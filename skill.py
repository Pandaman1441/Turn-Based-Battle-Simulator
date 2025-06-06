from abc import ABC, abstractmethod


class Skill(ABC):
    def __init__(self, name, base_damage, description, cost):
        self._name = name
        self._base_damage = base_damage
        self.__description = description
        self._cost = cost

    def get_info(self):
        desc = f"{self.__name}: {self.__description} \nCost: {self.__cost}"
        return desc
    
    @abstractmethod
    def use(self, user, target):
        pass
 

    # skills are loaded by string in the character object, we don't keep a reference of the skill objects 
    # and just call them by matching string names then immediatly use them. they are then garbage collected afterwards