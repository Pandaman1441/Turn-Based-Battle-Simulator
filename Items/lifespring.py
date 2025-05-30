from Items.item_class import Item




class Lifespring(Item):
    def __init__(self):
        super().__init__(name = "Lifespring",
        stats = {
            "r": 500
        },
        description = "test.",
        cost = 450,
        build = ["Mana Crystal", "Mana Crystal"],
        icon = "Assests/item_icons/misc/tile007.png")
