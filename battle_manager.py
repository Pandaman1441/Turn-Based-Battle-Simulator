import combat
import time

class Battle_Manager():
    def __init__(self, player_team, enemy_team):
        self.__p_party = player_team
        self.__e_party = enemy_team
        self.entities = self.__p_party + self.__e_party
        self.__turn_idx = 0
        self.__round = 1
        for i in self.entities:
            combat.roll_inititive(i)
        self.turn_order = sorted(self.entities, key=lambda character: character.inititive)
        self.turn_order.reverse()

    def current_turn(self):
        current = self.turn_order[0]
        if current.is_alive():
            print(f"--- Round {self.__round} | Turn {self.__turn_idx + 1} ---")
            print(f"{current.name}'s current turn\n")
        else:
            print(f"{current.name} is dead. Skipping...\n")
        return current

    def next_turn(self):
        current = self.turn_order.pop(0)

        if current.is_alive():
            self.turn_order.append(current)
        # Dead characters are not re-added

        self.__turn_idx += 1

        # Check if a full round has passed
        if self.__turn_idx % len(self.entities) == 0:
            self.__round += 1
    

    
    

# Turn order testing
from Classes import *
import generate_enemies

a = artificer.Artificer()
b = barbarian.Barbarian()
c = cleric.Cleric()
r = ranger.Ranger()
p_party = []
p_party.append(a)
p_party.append(b)
p_party.append(c)
p_party.append(r)

e1 = generate_enemies.Goblin()
e2 = generate_enemies.Goblin()
e3 = generate_enemies.Goblin()
e_party = []
e_party.append(e1)
e_party.append(e2)
e_party.append(e3)


m = Battle_Manager(p_party, e_party)

for _ in range(14):
    m.current_turn()
    m.next_turn()
