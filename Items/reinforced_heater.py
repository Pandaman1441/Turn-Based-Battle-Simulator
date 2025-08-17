from Items.item_class import Item




class Reinforced_Heater(Item):
    def __init__(self):
        super().__init__(name = "Reinforced Heater",
        stats = {
            "pr": 45
        },
        description = "test.",
        cost = 1000,
        build = ["Buckler", "Buckler"],
        icon = "Assets/item_icons/tile012.png")

