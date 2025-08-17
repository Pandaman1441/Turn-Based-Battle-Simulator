from Items.item_class import Item




class Sticker(Item):
    def __init__(self):
        super().__init__(name = "Sticker",
        stats = {
            "crit_chance": 20
        },
        description = "test.",
        cost = 800,
        build = ["Razor Fang", "Razor Fang"],
        icon = "Assets/item_icons/tile065.png") 
