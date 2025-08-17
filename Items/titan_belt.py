from Items.item_class import Item




class Titan_Belt(Item):
    def __init__(self):
        super().__init__(name = "Titan's Belt",
        stats = {
            "pp": 20,
            "hp": 300
        },
        description = "test.",
        cost = 1200,
        build = ["Recruit's Sword", "Heartstone"],
        icon = "Assets/item_icons/general/tile009.png")

