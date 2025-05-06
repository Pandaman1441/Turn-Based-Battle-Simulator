from Screens import battle_ui
from Screens import main_menu
from Screens import party
from Screens import shop


class manager:
    def __init__(self, pc):
        self.pc = pc
        self.screens = {
                        "battle" : battle_ui.b_UI(pc),
                        "menu" : main_menu.menu(pc),
                        "shop" : shop.Shop(pc),
                        "party" : party.Party(pc)
           }
        self.current = self.screens["menu"]
        self.__running = True

    def handle_event(self, event):
        fg = self.current.handle_event(event)
        if fg:
            if fg == "quit":
                self.__running = False
            elif fg in self.screens:
                self.current = self.screens[fg]
    
    def draw(self, screen):
        self.current.draw(screen)

    def get_status(self):
        return self.__running