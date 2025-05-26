from Items.item_class import Item




class Reinforced_Heater(Item):
    def __init__(self):
        super().__init__(name = "Reinforced Heater",
        stats = {
            "pr": 40
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile012.png")

