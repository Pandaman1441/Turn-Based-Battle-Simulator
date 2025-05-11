from Items.item_class import Item




class Ironclaw(Item):
    def __init__(self):
        self.__name = "Ironclaw"
        self.__stats = {
            "pp": 55,
            "hp": 1200
        }
        self.__description = "A people never forgotten"
        self.__cost = 3200
        self.__build = ["Titan's Belt", "Savage Axe", "Heartstone"]
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