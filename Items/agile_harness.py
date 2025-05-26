from Items.item_class import Item




class Agile_Harness(Item):
    def __init__(self):
        super().__init__(
            name = "Agile Harness",
            stats = {
                "ag": 30,
                "hp": 400
            },
            description = "test.",
            cost = 1,
            build = [],
            icon = "Assests/item_icons/tile077.png"
        )
    