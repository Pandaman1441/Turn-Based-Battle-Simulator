from Items.item_class import Item




class Titan_Belt(Item):
    def __init__(self):
        self.__name = "Titan's Belt"
        self.__stats = {
            "pp": 20,
            "hp": 650
        }
        self.__description = "test."
        self.__cost = 1250
        self.__build = ["Recruit's Sword", "Heartstone"]
        self.__icon = "Assests/item_icons/R.png"

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