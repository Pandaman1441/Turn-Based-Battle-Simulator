from Items.item_class import Item


class Savage_Axe(Item):
    def __init__(self):
        super().__init__(name = "Savage Axe",
        stats = {
            "pp": 25
        },
        description = "test.",
        cost = 750,
        build = [],
        icon = "Assets/item_icons/tile016.png"
)
