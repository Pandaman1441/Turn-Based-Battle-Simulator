from Items.item_class import Item




class Arcane_Focus(Item):
    def __init__(self):
        self.__name = "Arcane Focus"
        self.__stats = {
            "mp": 45
        }
        self.__description = "test."
        self.__cost = 810
        self.__build = []
        self.__icon = "Assests/item_icons/misc/tile003.png"

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