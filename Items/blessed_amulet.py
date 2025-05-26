from Items.item_class import Item




class Blessed_Amulet(Item):
    def __init__(self):
        super().__init__(
        name = "Blessed Amulet",
        stats = {
            "wp": 40
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile041.png"
)