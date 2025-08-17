from Items.item_class import Item




class Quickdraw_Pouch(Item):
    def __init__(self):
        super().__init__(name = "Quickdraw Pouch",
        stats = {
            "crit_chance": 10,
            "ag": 25
            },
        description = "test.",
        cost = 1200,
        build = ["Razor Fang", "Initiate's Dagger"],
        icon = "Assets/item_icons/potions/tile000.png")
