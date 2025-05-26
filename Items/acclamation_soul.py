from Items.item_class import Item


class Acclamation_Soul(Item):
    def __init__(self):
        super().__init__(
            name = "Acclamation of the Soul",
            stats = {},
            description = "The act of applause is an...",
            cost = 1,
            build = [],
            icon = "Assests/item_icons/placeholder.png"
        )