from Items.item_class import Item




class Heartstone(Item):
    def __init__(self):
        super().__init__(name = "Heartstone",
        stats = {"hp": 200
        },
        description = "test.",
        cost = 400,
        build = [],
        icon = "Assets/item_icons/potions/tile008.png")
