from Items.item_class import Item


class Ebon_Promise(Item):
    def __init__(self):
        super().__init__(name = "An Ebon Promise",
        stats = {},
        description = "Somethings never die.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
