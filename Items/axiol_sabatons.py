from Items.item_class import Item




class Axiol_Sabatons(Item):
    def __init__(self):
        super().__init__(
        name = "Axiol Sabatons",
        stats = {
            "pr": 25,
            "mr": 25
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile082.png")
