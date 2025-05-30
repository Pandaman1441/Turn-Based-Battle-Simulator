from Items.item_class import Item




class Barnacled_Greaves(Item):
    def __init__(self):
        super().__init__(
        name = "Barnacled Greaves",
        stats = {
            "pr": 20,
            "wp": 30
        },
        description = "test.",
        cost = 950,
        build = ["Buckler", "Bone Necklace"],
        icon = "Assests/item_icons/tile075.png")

  