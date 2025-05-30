from Items.item_class import Item




class Ancestor_Totem(Item):
    def __init__(self):
        super().__init__(
            name = "Ancestor Totem",
            stats = {
                "hp": 400,
                "wp": 20,
            },
            description = "test.",
            cost = 1150,
            build = ["Heartstone", "Bone Necklace"],
            icon = "Assests/item_icons/misc/tile000.png"
        )

