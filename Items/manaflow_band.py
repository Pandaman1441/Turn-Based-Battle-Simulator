from Items.item_class import Item




class Manaflow_Band(Item):
    def __init__(self):
        super().__init__(name = "Manaflow Band",
        stats = {
            "mp": 30,
            "r": 400
        },
        description = "test.",
        cost = 950,
        build = ["Mystic Tome", "Mana Crystal"],
        icon = "Assets/item_icons/general/tile046.png")
