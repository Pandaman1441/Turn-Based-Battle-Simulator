from Items.item_class import Item




class Ancestor_Totem(Item):
    def __init__(self):
        super().__init__(
            name = "Ancestor Totem",
            stats = {
                "hp": 550,
                "wp": 30,
            },
            description = "test.",
            cost = 1,
            build = [],
            icon = "Assests/item_icons/misc/tile000.png"
        )

