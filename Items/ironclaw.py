from Items.item_class import Item




class Ironclaw(Item):
    def __init__(self):
        super().__init__(name = "Ironclaw",
        stats = {
            "pp": 55,
            "hp": 1200
        },
        description = "A people never forgotten",
        cost = 3200,
        build = ["Titan's Belt", "Savage Axe", "Heartstone"],
        icon = "Assets/item_icons/tile069.png")

