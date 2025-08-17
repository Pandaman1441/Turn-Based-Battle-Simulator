from Items.item_class import Item




class Flowing_Cloak(Item):
    def __init__(self):
        super().__init__(name = "Flowing Cloak",
        stats = {
            "ag": 30
        },
        description = "test.",
        cost = 1000,
        build = [],
        icon = "Assets/item_icons/general/tile024.png")

  