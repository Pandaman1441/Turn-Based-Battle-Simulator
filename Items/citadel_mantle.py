from Items.item_class import Item




class Citadel_Mantle(Item):
    def __init__(self):
        super().__init__(name = "Citadel Mantle",
        stats = {
            "mr": 40
        },
        description = "test.",
        cost = 850,
        build = ["Anti-Magic Cloak","Anti-Magic Cloak"],
        icon = "Assests/item_icons/general/tile023.png")

   