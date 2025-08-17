from Items.item_class import Item


class Kingbreaker(Item):
    def __init__(self):
        super().__init__(name = "Kingbreaker",
        stats = {},
        description = "Cut kings to level.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
