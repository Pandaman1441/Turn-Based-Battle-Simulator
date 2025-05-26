from Items.item_class import Item




class Lifespring(Item):
    def __init__(self):
        super().__init__(name = "Lifespring",
        stats = {
            "r": 750
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/misc/tile007.png")
