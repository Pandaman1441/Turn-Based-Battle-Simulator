from Items.item_class import Item




class Marcher_Charm(Item):
    def __init__(self):
        super().__init__(name = "Marcher's Charm",
        stats = {
            "r": 500,
            "ag": 35
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/general/tile009.png")

