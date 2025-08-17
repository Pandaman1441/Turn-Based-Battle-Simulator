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
        icon = "Assets/item_icons/tile028.png")

