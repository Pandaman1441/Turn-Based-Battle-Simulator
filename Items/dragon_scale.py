from Items.item_class import Item




class Dragon_Scale(Item):
    def __init__(self):
        super().__init__(name = "Dragon Scale",
        stats = {
            "pr": 25,
            "hp": 300
        },
        description = "test.",
        cost = 1000,
        build = ["Buckler", "Heartstone"],
        icon = "Assests/item_icons/tile067.png")

  