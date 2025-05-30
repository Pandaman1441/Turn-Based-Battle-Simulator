from Items.item_class import Item




class Axiol_Sabatons(Item):
    def __init__(self):
        super().__init__(
        name = "Axiol Sabatons",
        stats = {
            "pr": 30,
            "mr": 30
        },
        description = "test.",
        cost = 1100,
        build = ["Buckler", "Anti-Magic Cloak"],
        icon = "Assests/item_icons/tile082.png")
