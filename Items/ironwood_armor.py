from Items.item_class import Item




class Ironwood_Armor(Item):
    def __init__(self):
        self.__name = "Ironwood Armor"
        self.__stats = {
            "pr": 30,
            "r": 550
        }
        self.__description = "test."
        self.__cost = 1
        self.__build = []
        self.__icon = "Assests/item_icons/tile004.png"

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