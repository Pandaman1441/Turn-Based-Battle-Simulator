import pygame
from UI_backend import button


class Shop:
    def __init__(self, pc):
        self.button = button.Button("Place Holder", (620,450), 200, 100)
        self.button.selected(True)
        self.pc = pc

    def draw(self,screen):
        screen.fill("orange")
        self.button.draw(screen)

    def handle_event(self, event):
        if event.key == pygame.K_RETURN:
            if self.button.get_selected():
                return "menu"