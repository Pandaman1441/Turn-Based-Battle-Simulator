from Items.item_class import Item




class Veteran_Greatsword(Item):
    def __init__(self):
        self.__name = "Veteran's Greatsword"
        self.__stats = {
            "pp": 45
        }
        self.__description = "test."
        self.__cost = 1350
        self.__build = ["Recruit's Sword", "Savage Axe"]
        self.__icon = "Assests/item_icons/tile021.png"

    @property
    def stats(self):
        return self.__stats
    
    @property
    def cost(self):
        return self.__cost
    
    @property
    def name(self):
        return self.__name
    
    @property
    def description(self):
        return self.__description
    
    @property
    def build(self):
        return self.__build
    
    @property
    def icon(self):
        return self.__icon