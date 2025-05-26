from Items.item_class import Item




class Citadel_Mantle(Item):
    def __init__(self):
        super().__init__(name = "Citadel Mantle",
        stats = {
            "mr": 35
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/general/tile023.png")

   