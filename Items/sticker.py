from Items.item_class import Item




class Sticker(Item):
    def __init__(self):
        super().__init__(name = "Sticker",
        stats = {
            "crit_chance": 20
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/general/tile002.png")
