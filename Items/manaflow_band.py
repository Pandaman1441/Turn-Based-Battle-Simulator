from Items.item_class import Item




class Manaflow_Band(Item):
    def __init__(self):
        super().__init__(name = "Manaflow Band",
        stats = {
            "mp": 35,
            "r": 500
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/general/tile046.png")
