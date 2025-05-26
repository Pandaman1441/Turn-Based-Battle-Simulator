from Items.item_class import Item


class Tanaka_Stopper(Item):
    def __init__(self):
        super().__init__(name = "Tanaka's Stopper",
        stats = {},
        description = "Maybe it can solve every problem.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/placeholder.png")

