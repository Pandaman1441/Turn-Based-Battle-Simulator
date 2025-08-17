from Items.item_class import Item




class Blessed_Amulet(Item):
    def __init__(self):
        super().__init__(
        name = "Blessed Amulet",
        stats = {
            "wp": 70
        },
        description = "test.",
        cost = 1250,
        build = ["Bone Necklace", "Familiar Sigil"],
        icon = "Assets/item_icons/tile041.png"
)

