from Items.item_class import Item




class Arcane_Barrier(Item):
    def __init__(self):
        super().__init__(
            name = "Arcane Barrier",
            stats = {
                "mr": 20,
                "r": 400
            },
            description = "test.",
            cost = 700,
            build = ["Anti-Magic Cloak", "Mana Crystal"],
            icon = "Assests/item_icons/tile053.png"
            )
