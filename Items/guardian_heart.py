from Items.item_class import Item




class Guardian_Heart(Item):
    def __init__(self):
        super().__init__(name = "Guardian's Heart",
        stats = {
            "mr": 30,
            "hp": 600
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile005.png")

  