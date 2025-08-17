from Items.item_class import Item


class Ink_Stained_Gloves(Item):
    def __init__(self):
        super().__init__(name = "Ink Stained Gloves",
        stats = {},
        description = "So much history, too little time to write.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")

