from Items.item_class import Item




class Dirk(Item):
    def __init__(self):
        self.__name = "Dirk"
        self.__stats = {
            "pp": 15,
            "ag": 20
        }
        self.__description = "test."
        self.__cost = 1100
        self.__build = ["Recruit's Sword", "Initiate's Dagger"]
        self.__icon = "Assests/item_icons/tile084.png"

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