from Items.item_class import Item




class Flowing_Cloak(Item):
    def __init__(self):
        self.__name = "Flowing Cloak"
        self.__stats = {
            "ag": 30
        }
        self.__description = "test."
        self.__cost = 1000
        self.__build = []
        self.__icon = "Assests/item_icons/general/tile024.png"

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