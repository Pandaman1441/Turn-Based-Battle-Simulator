from Items.item_class import Item




class Barnacled_Greaves(Item):
    def __init__(self):
        super().__init__(
        name = "Barnacled Greaves",
        stats = {
            "pr": 25,
            "wp": 20
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile075.png")

  