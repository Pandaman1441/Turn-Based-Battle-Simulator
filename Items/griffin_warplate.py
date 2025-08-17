from Items.item_class import Item


class Griffin_Warplate(Item):
    def __init__(self):
        super().__init__(name = "Griffin Warplate",
        stats = {},
        description = "Pristine and ready to take flight.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
