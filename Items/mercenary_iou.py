from Items.item_class import Item


class Mercenary_IOU(Item):
    def __init__(self):
        super().__init__(name = "Mercenary's IOU",
        stats = {},
        description = "Payable upon survival.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/placeholder.png")
