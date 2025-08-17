from Items.item_class import Item


class Heart_Warlord(Item):
    def __init__(self):
        super().__init__(name = "Heart of the Warlord",
        stats = {},
        description = "Still beating and raging.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
