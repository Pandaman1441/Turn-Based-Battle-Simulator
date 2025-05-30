from Items.item_class import Item




class Resolved(Item):
    def __init__(self):
        super().__init__(name = "Resolved",
        stats = {
            "mr": 25,
            "wp": 25,
        },
        description = "test.",
        cost = 900,
        build = ["Anti-Magic Cloak", "Bone Necklace"],
        icon = "Assests/item_icons/tile081.png")

