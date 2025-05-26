from Items.item_class import Item




class Ironwood_Armor(Item):
    def __init__(self):
        super().__init__(name = "Ironwood Armor",
        stats = {
            "pr": 30,
            "r": 550
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile004.png")
