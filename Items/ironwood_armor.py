from Items.item_class import Item




class Ironwood_Armor(Item):
    def __init__(self):
        super().__init__(name = "Ironwood Armor",
        stats = {
            "pr": 20,
            "r": 400
        },
        description = "test.",
        cost = 800,
        build = ["Buckler", "Mana Crystal"],
        icon = "Assests/item_icons/tile004.png")
