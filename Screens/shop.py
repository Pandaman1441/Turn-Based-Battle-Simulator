import pygame
from UI_backend import button, scroll_grid


class Shop:
    def __init__(self, pc):
        self.__back = button.Button("Back", (30,770), 200, 100)
        self.__back.selected(True)
        self.__party = button.Button("Party", (1210, 770), 200, 100)
        self.__pc = pc
        self.__shop = scroll_grid.Scroll_Grid(self.__pc)
        

        self.__inner = False                # inside shop list
        self.__outer = False                # hover shop list
        self.__inner_idx = 0                # shop selected index


    def draw(self,screen):
        screen.fill("orange")
        self.__back.draw(screen)
        self.__party.draw(screen)
        self.__shop.draw(screen)
            

    def handle_event(self, event):
        if self.__shop.inner:
            r = self.__shop.handle_event(event)
            if r:
                self.__back.selected(True)

        else:
            if event.key == pygame.K_RETURN:
                if self.__back.get_selected():
                    return "menu"
                elif self.__shop.outer:
                    self.__shop.inner = True
                    self.__shop.shop = True
                elif self.__party.get_selected():
                    return "party"

            elif event.key == pygame.K_ESCAPE:
                self.__back.selected(True)
                self.__shop.outer = False
                self.__shop.inner = False
                self.__shop.inner_idx = 0
                self.__party.selected(False)
                for b in self.__shop.buttons:
                    b.selected(False)    

            elif event.key == pygame.K_LEFT:
                if not self.__shop.inner:
                    if self.__shop.outer:
                        self.__back.selected(True)
                        self.__shop.outer = False
                    elif self.__party.get_selected():
                        self.__party.selected(False)
                        self.__shop.outer = True
                
            elif event.key == pygame.K_RIGHT:
                if not self.__shop.inner:
                    if self.__back.get_selected():
                        self.__shop.outer = True
                        self.__back.selected(False)
                    elif self.__shop.outer:
                        self.__shop.outer = False
                        self.__party.selected(True)
            
        
        
    