from Items.item_class import Item


class Blank_Contract(Item):
    def __init__(self):
        super().__init__(
        name = "Blank Contract",
        stats = {},
        description = "The paper is blank until the knife drips.",
        cost = 1,
        build = [],
        icon = "Assets/item_icons/placeholder.png")

   