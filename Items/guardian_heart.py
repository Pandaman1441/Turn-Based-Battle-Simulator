from Items.item_class import Item




class Guardian_Heart(Item):
    def __init__(self):
        super().__init__(name = "Guardian's Heart",
        stats = {
            "mr": 20,
            "hp": 400
        },
        description = "test.",
        cost = 1200,
        build = ["Anti-Magic Cloak", "Heartstone"],
        icon = "Assets/item_icons/tile005.png")

  