from Items.item_class import Item




class Buckler(Item):
    def __init__(self):
        super().__init__(name = "Buckler",
        stats = {
            "pr": 15
        },
        description = "test.",
        cost = 300,
        build = [],
        icon = "Assets/item_icons/tile011.png")

   