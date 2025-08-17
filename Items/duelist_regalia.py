from Items.item_class import Item


class Duelist_Regalia(Item):
    def __init__(self):
        super().__init__(name = "Duelist's Regalia",
        stats = {},
        description = "For those who can sign their name in steel.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")

    