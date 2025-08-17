from Items.item_class import Item


class Emberheart(Item):
    def __init__(self):
        super().__init__(name = "Emberheart",
        stats = {},
        description = "Who needs a forge?",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
