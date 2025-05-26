from Items.item_class import Item


class Pinnacle(Item):
    def __init__(self):
        super().__init__(name = "Pinnacle",
        stats = {},
        description = "This is my peak, this is...",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/placeholder.png"
)