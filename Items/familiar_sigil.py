from Items.item_class import Item




class Familiar_Sigil(Item):
    def __init__(self):
        self.__name = "Familiar Sigil"
        self.__stats = {
            "wp": 40
        }
        self.__description = "test."
        self.__cost = 700
        self.__build = []
        self.__icon = "Assests/item_icons/tile081.png"

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