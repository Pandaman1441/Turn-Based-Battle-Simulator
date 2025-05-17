from Items.item_class import Item




class Guardian_Heart(Item):
    def __init__(self):
        self.__name = "Guardian's Heart"
        self.__stats = {
            "mr": 30,
            "hp": 600
        }
        self.__description = "test."
        self.__cost = 1
        self.__build = []
        self.__icon = "Assests/item_icons/tile005.png"

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