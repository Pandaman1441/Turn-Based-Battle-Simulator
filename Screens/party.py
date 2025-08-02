from UI_backend import button
import pygame
from UI_backend import button, selector
from Classes import *


class Party:
    def __init__(self, pc):
        self.__button = button.Button("Place Holder", (620,450), 200, 100)
        self.__button.selected(True)
        self.__pc = pc
        self.__classes = ["artificer", "assassin", "barbarian", "bladeslinger", "cleric", "mercenary", "monk", "paladin", "ranger", "scholar", "sorceress", "thief"]
        self.__selector = selector.Selector(self.__classes,(595, 700))           # 250 px wide 50 px tall


    def draw(self,screen):
        screen.fill("orange")
        self.__button.draw(screen)
        self.__selector.draw(screen)

    def handle_event(self, event):
        if event.key == pygame.K_RETURN:
            if self.__button.get_selected():
                return "menu"
            if self.__selector.get_selected():
                x = self.__selector.get_choice()
                self.class_selection(x)
                

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
                self.__pc.append(artificer.Artificer())
            case 1:
                self.__pc.append(assassin.Assassin())
            case 2:
                self.__pc.append(barbarian.Barbarian())
            case 3:
                self.__pc.append(bladeslinger.Bladeslinger())
            case 4:
                self.__pc.append(cleric.Cleric())
            case 5:
                self.__pc.append(mercenary.Mercenary())
            case 6:
                self.__pc.append(monk.Monk())
            case 7:
                self.__pc.append(paladin.Paladin())
            case 8:
                self.__pc.append(ranger.Ranger())
            case 9:
                self.__pc.append(scholar.Scholar())
            case 10:
                self.__pc.append(sorceress.Sorceress())
            case 11:
                self.__pc.append(thief.Thief())
