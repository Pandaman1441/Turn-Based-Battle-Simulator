from Items.item_class import Item


class Light_Hope_Beacon(Item):
    def __init__(self):
        super().__init__(name = "Light's Hope Beacon",
        stats = {},
        description = "A gentle answer to darkness.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
