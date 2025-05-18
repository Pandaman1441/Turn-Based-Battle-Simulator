from Items.item_class import Item




class Hexed_Maul(Item):
    def __init__(self):
        self.__name = "Hexed Maul"
        self.__stats = {
            "pp": 20,
            "mr": 20
        }
        self.__description = "test."
        self.__cost = 950
        self.__build = []
        self.__icon = "Assests/item_icons/tile030.png"

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