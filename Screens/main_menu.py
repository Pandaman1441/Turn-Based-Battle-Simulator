import pygame
from Classes import *
from UI_backend import button, selector



classes = ["artificer", "assassin", "barbarian", "bladeslinger", "cleric", "mercenary", "monk", "paladin", "ranger", "scholar", "sorceress", "thief"]


class menu:
    def __init__(self):
        self.button = button.Button("Battle!", (620,450), 200, 100)
        self.selector = selector.Selector(classes,(595, 700))           # 250 px wide 50 px tall
        self.button.selected(True)



    def draw(self, screen):
        screen.fill("purple")
        self.button.draw(screen)
        self.selector.draw(screen)

    def handle_event(self,event):
        if event.key == pygame.K_RETURN:
            if self.button.get_selected():
                return "battle" 
            elif self.selector.get_selected():
                x = self.selector.get_choice()
                self.class_selection(x)

        elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            if self.selector.get_selected():
                self.selector.handle_event(event)

        elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            if self.button.get_selected():
                self.button.selected(False)
                self.selector.selected(True)
            else:
                self.button.selected(True)
                self.selector.selected(False)
        
           




    def class_selection(self, value):
        archetypes = [("artificer",0), ("assassin", 1), ("barbarian", 2), ("bladeslinger", 3), ("cleric", 4), ("mercenary", 5), ("monk", 6), ("paladin", 7), ("ranger", 8), ("scholar", 9), ("sorceress", 10), ("thief", 11) ]

        match value:
            case 0:
                p1 = artificer.Artificer()
                print(f"You have chosen: {p1.name}")
            case 1:
                p1 = assassin.Assassin()
                print(f"You have chosen: {p1.name}")
            case 2:
                p1 = barbarian.Barbarian()
                print(f"You have chosen: {p1.name}")
            case 3:
                p1 = bladeslinger.Bladeslinger()
                print(f"You have chosen: {p1.name}")
            case 4:
                p1 = cleric.Cleric()
                print(f"You have chosen: {p1.name}")
            case 5:
                p1 = mercenary.Mercenary()
                print(f"You have chosen: {p1.name}")
            case 6:
                p1 = monk.Monk()
                print(f"You have chosen: {p1.name}")
            case 7:
                p1 = paladin.Paladin()
                print(f"You have chosen: {p1.name}")
            case 8:
                p1 = ranger.Ranger()
                print(f"You have chosen: {p1.name}")
            case 9:
                p1 = scholar.Scholar()
                print(f"You have chosen: {p1.name}")
            case 10:
                p1 = sorceress.Sorceress()
                print(f"You have chosen: {p1.name}")
            case 11:
                p1 = thief.Thief()
                print(f"You have chosen: {p1.name}")

