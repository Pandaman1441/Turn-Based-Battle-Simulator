from Items.item_class import Item




class Mana_Crystal(Item):
    def __init__(self):
        super().__init__(name = "Mana Crystal",
        stats = {
            "r": 300
        },
        description = "test.",
        cost = 300,
        build = [],
        icon = "Assests/item_icons/potions/tile017.png")
