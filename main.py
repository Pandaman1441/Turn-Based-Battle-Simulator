from Classes import *
import random
import time
import pygame
from UI_backend import button
from UI_backend import battle_ui




archetypes = ["artificer", "assassin", "barbarian", "bladeslinger", "cleric", "mercenary", "monk", "paladin", "ranger", "scholar", "sorceress", "thief" ]

pygame.init()
screen = pygame.display.set_mode((1440, 900))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
running = True

action = button.Button("hello world", (50,700), 500, 100)
thing = battle_ui.b_UI()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    x = pygame.image.load("Assests/background.j" \
    "pg")
    bg = pygame.Surface.convert(x)
    screen.blit(bg,(0,0))
    
    thing.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# def main():
#     print("\nChoose a class from the options below: ")
#     for i, cls in enumerate(archetypes, start=0):
#         print(f"{i}. {cls}")
#     c = int(input("Enter your choice here: "))

#     match c:
#         case 0:
#             p1 = artificer.Artificer()
#         case 1:
#             p1 = assassin.Assassin()
#         case 2:
#             p1 = barbarian.Barbarian()
#         case 3:
#             p1 = bladeslinger.Bladeslinger
#         case 4:
#             p1 = cleric.Cleric()
#         case 5:
#             p1 = mercenary.Mercenary
#         case 6:
#             p1 = monk.Monk()
#         case 7:
#             p1 = paladin.Paladin()
#         case 8:
#             p1 = ranger.Ranger()
#         case 9:
#             p1 = scholar.Scholar()
#         case 10:
#             p1 = sorceress.Sorceress()
#         case 11:
#             p1 = thief.Thief()

#     while True:
#         p1.intro()
#         print("\n")

#         print("\n---- MENU ----")
#         print("1. Change Character")
#         print("2. Basic Attack")
#         print("3. Abilities")
#         print("4. Exit")
#         r = int(input("\nSelect an option: "))

#         time.sleep(.5)

#         if r == 4:
#             print("Goodbye")
#             break
#         else:
#             print("\nUnder Construction")
        
        



# if __name__ == "__main__":
#     main()




