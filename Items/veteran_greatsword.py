from Items.item_class import Item




class Veteran_Greatsword(Item):
    def __init__(self):
        super().__init__(name = "Veteran's Greatsword",
        stats = {
            "pp": 45
        },
        description = "test.",
        cost = 1350,
        build = ["Recruit's Sword", "Savage Axe"],
        icon = "Assets/item_icons/tile021.png")

