from Items.item_class import Item


class Hexed_Counter_Matrix(Item):
    def __init__(self):
        super().__init__(name = "Hexed Counter Matrix",
        stats = {},
        description = "THE failsafe against runaway magic - only occasionally fizzles reality.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")
