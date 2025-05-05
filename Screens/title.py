import pygame
from Classes import *
from UI_backend import button, selector





class Title:
    def __init__(self):
        self.__button = button.Button("Hello World!", (620,450), 200, 100)
        self.__button.selected(True)
        self.__classes = ["artificer", "assassin", "barbarian", "bladeslinger", "cleric", "mercenary", "monk", "paladin", "ranger", "scholar", "sorceress", "thief"]
        self.__selector = selector.Selector(self.__classes,(595, 700))           # 250 px wide 50 px tall
        self.__pc = None



    def draw(self, screen):
        screen.fill("purple")
        self.__button.draw(screen)
        self.__selector.draw(screen)

    def handle_event(self,event):
        if event.key == pygame.K_RETURN:
            if self.__selector.get_selected():
                x = self.__selector.get_choice()
                self.class_selection(x)
                return self.__pc

        elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            if self.__selector.get_selected():
                self.__selector.handle_event(event)

        elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            if self.__button.get_selected():
                self.__button.selected(False)
                self.__selector.selected(True)
            else:
                self.__button.selected(True)
                self.__selector.selected(False)

    def class_selection(self, value):

        match value:
            case 0:
                self.__pc = artificer.Artificer()
            case 1:
                self.__pc = assassin.Assassin()
            case 2:
                self.__pc = barbarian.Barbarian()
            case 3:
                self.__pc = bladeslinger.Bladeslinger()
            case 4:
                self.__pc = cleric.Cleric()
            case 5:
                self.__pc = mercenary.Mercenary()
            case 6:
                self.__pc = monk.Monk()
            case 7:
                self.__pc = paladin.Paladin()
            case 8:
                self.__pc = ranger.Ranger()
            case 9:
                self.__pc = scholar.Scholar()
            case 10:
                self.__pc = sorceress.Sorceress()
            case 11:
                self.__pc = thief.Thief()

