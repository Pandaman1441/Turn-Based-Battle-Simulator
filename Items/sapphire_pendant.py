from Items.item_class import Item




class Sapphire_Pendant(Item):
    def __init__(self):
        super().__init__(name = "Sapphire Pendant",
        stats = {
            "mp": 30,
            "wp": 45
        },
        description = "test.",
        cost = 1400,
        build = ["Mystic Tome", "Familiar Sigil"],
        icon = "Assests/item_icons/general/tile046.png")
