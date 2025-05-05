from Screens import battle_ui
from Screens import title
from Screens import main_menu

class manager:
    def __init__(self, pc):
        self.pc = pc
        self.screens = {
                        "battle" : battle_ui.b_UI(pc),
                        "menu" : main_menu.menu(pc)
           }
        self.current = self.screens["menu"]

    def handle_event(self, event):
        fg = self.current.handle_event(event)
        if fg:
            if fg in self.screens:
                self.current = self.screens[fg]
    
    def draw(self, screen):
        self.current.draw(screen)