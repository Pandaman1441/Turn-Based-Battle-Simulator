from Items.item_class import Item




class Horned_Helm(Item):
    def __init__(self):
        super().__init__(name = "Horned Helm",
        stats = {
            "pp": 15,
            "pr": 20
        },
        description = "test.",
        cost = 850,
        build = ["Buckler", "Recruit's Sword"],
        icon = "Assets/item_icons/tile054.png")
