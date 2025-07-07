


class Battle_Manager():
    def __init__(self, player_team, enemy_team):
        self.__p_party = player_team
        self.__e_party = enemy_team
        self.__turn_order = self.__p_party + self.__e_party
        self.__turn_idx = 0

    def current_turn(self):
        return self.__turn_order[self.__turn_idx]
    
    