from Items.item_class import Item


class Dragonspine_Bulwark(Item):
    def __init__(self):
        super().__init__(name = "Dragon's Spine Bulwark",
        stats = {},
        description = "A piece of the first stone of the Dragon's Spine.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
