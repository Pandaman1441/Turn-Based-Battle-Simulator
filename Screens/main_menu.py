from UI_backend import button
import pygame

class menu:
    def __init__(self, pc):
        self.__battle = button.Button("Battle!", (620,450), 200, 100)
        self.__shop = button.Button('Shop', (620, 560), 200, 100)
        self.__party = button.Button('Party', (620, 670), 200, 100)
        self.__exit = button.Button('Quit', (620, 780), 200, 100)

        self.__pc = pc
        self.__buttons = [self.__battle, self.__shop, self.__party, self.__exit]
        self.__selected_idx = 0
        self.__buttons[self.__selected_idx].selected(True)

    def draw(self,screen):
        screen.fill("orange")
        self.__battle.draw(screen)
        self.__shop.draw(screen)
        self.__party.draw(screen)
        self.__exit.draw(screen)

    def handle_event(self, event):
        ps = self.__selected_idx
        if event.key == pygame.K_RETURN:
            if self.__battle.get_selected():
                return "battle"
            elif self.__shop.get_selected():
                return "shop"
            elif self.__party.get_selected():
                return "party"
            elif self.__exit.get_selected():
                return "quit"
        elif event.key == pygame.K_DOWN:
            ps = (ps + 1) % len(self.__buttons)
        elif event.key == pygame.K_UP:
            ps = (ps - 1) % len(self.__buttons)

        self.__buttons[self.__selected_idx].selected(False)

        self.__selected_idx = ps
        self.__buttons[ps].selected(True)