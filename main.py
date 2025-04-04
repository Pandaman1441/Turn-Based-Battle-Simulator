import Classes
import random

import Classes.barbarian
import Classes.fighter

archetypes = ["artificer", "assassin", "barbarian", "bard", "cleric", "fighter", "monk", "paladin", "ranger", "rogue", "sorceress", "wizard", ]

def main():
    print("\nChoose a class from the options below: ")
    for i, cls in enumerate(archetypes, start=0):
        print(f"{i}. {cls}")
    c = int(input("Enter your choice here: "))

    match c:
        case 1:
            p1 = Classes.fighter.Fighter()
        case 2:
            p1 = Classes.barbarian.

    

    p1.intro()
    print("\n")
    p1.display()

    while True:
        print("\n---- MENU ----")
        print("1. Change Character")
        print("2. Basic Attack")
        print("3. Abilities")
        print("4. Exit")
        r = int(input("\nSelect an option "))

        if r == 4:
            print("Goodbye")
            break
        else:
            print("\nUnder Construction")


if __name__ == "__main__":
    main()




