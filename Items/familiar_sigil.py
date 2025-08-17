from Items.item_class import Item




class Familiar_Sigil(Item):
    def __init__(self):
        super().__init__(name = "Familiar Sigil",
        stats = {
            "wp": 40
        },
        description = "test.",
        cost = 700,
        build = [],
        icon = "Assets/item_icons/tile081.png")
