from Screens import battle_ui
from Screens import main_menu
from Screens import party
from Screens import shop


class manager:
    def __init__(self, pc):
        self.__party = [pc]
        self.screens = {
                        "battle" : battle_ui.b_UI(self.__party,),
                        "menu" : main_menu.menu(self.__party),
                        "shop" : shop.Shop(self.__party),
                        "party" : party.Party(self.__party)
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
    
    def add_character(self, pc):
        if len(self.__party) < 5:
            self.__party.append(pc)
            print(self.__party)