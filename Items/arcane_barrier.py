from Items.item_class import Item




class Arcane_Barrier(Item):
    def __init__(self):
        super().__init__(
            name = "Arcane Barrier",
            stats = {
                "mr": 30,
                "r": 600
            },
            description = "test.",
            cost = 1,
            build = [],
            icon = "Assests/item_icons/tile053.png"
            )
