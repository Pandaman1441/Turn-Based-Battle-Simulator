from Items.item_class import Item




class Warding_Talisman(Item):
    def __init__(self):
        super().__init__(name = "Warding Talisman",
        stats = {
            "mp": 25,
            "mr": 35,
        },
        description = "test.",
        cost = 1100,
        build = ["Mystic Tome", "Anti-Magic Cloak"],
        icon = "Assets/item_icons/tile033.png")

