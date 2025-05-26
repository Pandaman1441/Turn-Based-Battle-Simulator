from Items.item_class import Item




class Warding_Talisman(Item):
    def __init__(self):
        super().__init__(name = "Warding Talisman",
        stats = {
            "mp": 30,
            "mr": 25,
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile033.png")

