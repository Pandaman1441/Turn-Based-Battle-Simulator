from Items.item_class import Item




class Resolved(Item):
    def __init__(self):
        super().__init__(name = "Resolved",
        stats = {
            "mr": 25,
            "wp": 35,
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile081.png")

