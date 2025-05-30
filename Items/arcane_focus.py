from Items.item_class import Item




class Arcane_Focus(Item):
    def __init__(self):
        super().__init__(
            name = "Arcane Focus",
            stats = {
                "mp": 45
            },
            description = "test.",
            cost = 850,
            build = [],
            icon = "Assests/item_icons/misc/tile003.png"
)
   