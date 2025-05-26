from Items.item_class import Item




class Mystic_Tome(Item):
    def __init__(self):
        super().__init__(name = "Mystic_Tome",
        stats = {
            "mp": 25
        },
        description = "test.",
        cost = 450,
        build = [],
        icon = "Assests/item_icons/tile019.png")

