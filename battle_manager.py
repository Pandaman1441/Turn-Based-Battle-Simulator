import combat


class Battle_Manager():
    def __init__(self, player_team, enemy_team):
        self.__p_party = player_team
        self.__e_party = enemy_team
        self.entities = self.__p_party + self.__e_party
        self.__turn_idx = 0
        self.__round = 0
        for i in self.entities:
            combat.roll_inititve(i)
        self.turn_order = sorted(self.entities, key=lambda character: character.inititive)
        self.turn_order.reverse()

    def current_turn(self):
        return self.turn_order[self.__turn_idx]
    
    

# Turn order testing
# from Classes import *
# import generate_enemies

# a = artificer.Artificer()
# b = barbarian.Barbarian()
# c = cleric.Cleric()
# r = ranger.Ranger()
# p_party = []
# p_party.append(a)
# p_party.append(b)
# p_party.append(c)
# p_party.append(r)

# e1 = generate_enemies.Goblin()
# e2 = generate_enemies.Goblin()
# e3 = generate_enemies.Goblin()
# e_party = []
# e_party.append(e1)
# e_party.append(e2)
# e_party.append(e3)


# m = Battle_Manager(p_party, e_party)
