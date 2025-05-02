from UI_backend import battle_ui
from Screens import main_menu


class manager:
    def __init__(self):
        self.screens = {"menu" : main_menu.menu(),
           "battle" : battle_ui.b_UI()
           }
        self.current = self.screens["menu"]

    def handle_event(self, event):
        fg = self.current.handle_event(event)
        if fg:
            if fg in self.screens:
                self.current = self.screens[fg]
    
    def draw(self, screen):
        self.current.draw(screen)