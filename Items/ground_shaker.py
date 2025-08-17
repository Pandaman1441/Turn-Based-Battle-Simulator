from Items.item_class import Item




class Ground_Shaker(Item):
    def __init__(self):
        super().__init__(name = "Ground Shaker",
        stats = {
        },
        description = "And so the ground trembles.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
