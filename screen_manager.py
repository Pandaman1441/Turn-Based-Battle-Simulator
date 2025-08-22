from Screens import battle_ui
from Screens import main_menu
from Screens import party
from Screens import shop


class manager:
    def __init__(self, pc):
        self.__party = [pc]
        self.current = main_menu.menu(self.__party)
        self.__running = True

    def handle_event(self, event):
        fg = self.current.handle_event(event)
        if fg:
            if fg == "quit":
                self.__running = False
            elif fg == "battle":
                self.current = battle_ui.b_UI(self.__party)
            elif fg == "menu":
                self.current = main_menu.menu(self.__party)
            elif fg == "shop":
                self.current = shop.Shop(self.__party)
            elif fg == "party":
                self.current = party.Party(self.__party)
    
    def draw(self, screen):
        self.current.draw(screen)

    def get_status(self):
        return self.__running
    
    def add_character(self, pc):
        if len(self.__party) < 5:
            self.__party.append(pc)
            print(self.__party)