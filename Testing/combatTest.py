import unittest
import combat
from character import Character







# assert(in question, correct)


class TestCombatMethods(unittest.TestCase):

    def immutableStats(self):
        # This was testing the copies making sure values aren't changed mid process
        p2 = Character()

        p2_stats = p2.get_all_stats()

        print("\np2: ")
        for key, value in p2_stats.items():
            print(f"{key}: {value}")

        print("\ndealing 10 damage to p2.\n")

        combat.damage_target(10, p2)
        print("\np2: ")
        value = p2.get_stat("hp")
        print(value)
