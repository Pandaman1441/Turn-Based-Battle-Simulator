from Items.item_class import Item


class Dragon_Thorns(Item):
    def __init__(self):
        super().__init__(name = "Dragon Thorns",
        stats = {},
        description = "Crafted by dragons or at least by their kin.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/placeholder.png")

    