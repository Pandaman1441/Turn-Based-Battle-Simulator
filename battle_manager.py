import combat


class Battle_Manager():
    def __init__(self, player_team, enemy_team):
        self.__p_party = player_team
        self.__e_party = enemy_team
        self.__entities = self.__p_party + self.__e_party
        self.__turn_idx = 0
        self.__round = 0
        for i in self.__entities:
            combat.roll_inititve(i)
        self.__turn_order = sorted(self.__entities, key=lambda character: character.inititive)

    def current_turn(self):
        return self.__turn_order[self.__turn_idx]
    
    