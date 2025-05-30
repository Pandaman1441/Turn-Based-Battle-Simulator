from Items.item_class import Item




class Agile_Harness(Item):
    def __init__(self):
        super().__init__(
            name = "Agile Harness",
            stats = {
                "hp": 300,
                "ag": 20
            },
            description = "test.",
            cost = 1000,
            build = ["Heartstone", "Initiate's Dagger"],
            icon = "Assests/item_icons/tile077.png"
        )
    