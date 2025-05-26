from Items.item_class import Item




class Quickdraw_Pouch(Item):
    def __init__(self):
        super().__init__(name = "Quickdraw Pouch",
        stats = {
            "crit_chance": 15,
            "ag": 20
            },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/potions/tile000.png")
