import pygame
from Classes import *
from UI_backend import button



archetypes = [("artificer",0), ("assassin", 1), ("barbarian", 2), ("bladeslinger", 3), ("cleric", 4), ("mercenary", 5), ("monk", 6), ("paladin", 7), ("ranger", 8), ("scholar", 9), ("sorceress", 10), ("thief", 11) ]

class menu:
    def __init__(self):
        self.button = button.Button("Battle!", (720,450), 200, 100)


    def draw(self, screen):
        screen.fill("purple")
        self.button.selected(True)
        self.button.draw(screen)

    def handle_event(self,event):
        if event.key == pygame.K_RETURN:
            return "battle"

# def class_selection(_, value):
#     match value:
#         case 0:
#             p1 = artificer.Artificer()
#             print(f"You have chosen: {p1.name}")
#         case 1:
#             p1 = assassin.Assassin()
#             print(f"You have chosen: {p1.name}")
#         case 2:
#             p1 = barbarian.Barbarian()
#             print(f"You have chosen: {p1.name}")
#         case 3:
#             p1 = bladeslinger.Bladeslinger()
#             print(f"You have chosen: {p1.name}")
#         case 4:
#             p1 = cleric.Cleric()
#             print(f"You have chosen: {p1.name}")
#         case 5:
#             p1 = mercenary.Mercenary()
#             print(f"You have chosen: {p1.name}")
#         case 6:
#             p1 = monk.Monk()
#             print(f"You have chosen: {p1.name}")
#         case 7:
#             p1 = paladin.Paladin()
#             print(f"You have chosen: {p1.name}")
#         case 8:
#             p1 = ranger.Ranger()
#             print(f"You have chosen: {p1.name}")
#         case 9:
#             p1 = scholar.Scholar()
#             print(f"You have chosen: {p1.name}")
#         case 10:
#             p1 = sorceress.Sorceress()
#             print(f"You have chosen: {p1.name}")
#         case 11:
#             p1 = thief.Thief()
#             print(f"You have chosen: {p1.name}")

