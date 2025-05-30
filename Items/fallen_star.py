from Items.item_class import Item




class Fallen_Star(Item):
    def __init__(self):
        super().__init__(name = "Fallen Star",
        stats = {
            "r": 400,
            "wp": 25
        },
        description = "test.",
        cost = 850,
        build = ["Mana Crystal", "Bone Necklace"],
        icon = "Assests/item_icons/potions/tile019.png")
