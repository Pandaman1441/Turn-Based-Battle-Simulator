from Items.item_class import Item




class Marcher_Charm(Item):
    def __init__(self):
        super().__init__(name = "Marcher's Charm",
        stats = {
            "ag": 20,
            "wp": 25
        },
        description = "test.",
        cost = 1100,
        build = ["Initiate's Dagger", "Bone Necklace"],
        icon = "Assets/item_icons/misc/tile002.png")

