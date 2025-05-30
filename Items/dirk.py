from Items.item_class import Item




class Dirk(Item):
    def __init__(self):
        super().__init__(name = "Dirk",
        stats = {
            "pp": 15,
            "ag": 20
        },
        description = "test.",
        cost = 1100,
        build = ["Recruit's Sword", "Initiate's Dagger"],
        icon = "Assests/item_icons/tile000.png") 

   