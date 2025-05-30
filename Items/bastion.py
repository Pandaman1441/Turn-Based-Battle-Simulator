from Items.item_class import Item




class Bastion(Item):
    def __init__(self):
        super().__init__(
        name = "Bastion",
        stats = {
            "hp": 550
        },
        description = "test.",
        cost = 1000,
        build = ["Heartstone", "Heartstone"],
        icon = "Assests/item_icons/tile040.png")
