from Classes import *
import random
import time

archetypes = ["artificer", "assassin", "barbarian", "bard", "cleric", "fighter", "monk", "paladin", "ranger", "rogue", "sorceress", "wizard", ]

def main():
    print("\nChoose a class from the options below: ")
    for i, cls in enumerate(archetypes, start=0):
        print(f"{i}. {cls}")
    c = int(input("Enter your choice here: "))

    match c:
        case 0:
            p1 = artificer.Artificer()
        case 1:
            p1 = assassin.Assassin()
        case 2:
            p1 = barbarian.Barbarian()
        case 3:
            p1 = bard.Bard()
        case 4:
            p1 = cleric.Cleric()
        case 5:
            p1 = fighter.Fighter()
        case 6:
            p1 = monk.Monk()
        case 7:
            p1 = paladin.Paladin()
        case 8:
            p1 = ranger.Ranger()
        case 9:
            p1 = rogue.Rogue()
        case 10:
            p1 = sorceress.Sorceress()
        case 11:
            p1 = wizard.Wizard()

    

    while True:
        p1.intro()
        print("\n")
        p1.display()

        print("\n---- MENU ----")
        print("1. Change Character")
        print("2. Basic Attack")
        print("3. Abilities")
        print("4. Exit")
        r = int(input("\nSelect an option: "))

        time.sleep(.5)

        if r == 4:
            print("Goodbye")
            break
        else:
            print("\nUnder Construction")
        
        


if __name__ == "__main__":
    main()




