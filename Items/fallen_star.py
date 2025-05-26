from Items.item_class import Item




class Fallen_Star(Item):
    def __init__(self):
        super().__init__(name = "Fallen Star",
        stats = {
            "r": 600,
            "wp": 25
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/potions/tile019.png")
