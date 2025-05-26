from Items.item_class import Item




class Verdant_Boots(Item):
    def __init__(self):
        super().__init__(name = "Verdant Boots",
        stats = {
            "ag": 25,
            "wp": 25,
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/misc/tile005.png"
)