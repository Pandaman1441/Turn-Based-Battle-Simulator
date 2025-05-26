from Items.item_class import Item




class Initiate_Dagger(Item):
    def __init__(self):
        super().__init__(name = "Initiate's Dagger",
        stats = {
            "ag": 15
        },
        description = "test.",
        cost = 500,
        build = [],
        icon = "Assests/item_icons/tile028.png")

