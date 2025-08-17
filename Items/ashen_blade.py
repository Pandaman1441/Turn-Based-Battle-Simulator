from Items.item_class import Item


class Ashen_Blade(Item):
    def __init__(self):
        super().__init__(
        name = "Ashen Blade",
        stats = {},
        description = "It speaks in secrets older than steel.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
