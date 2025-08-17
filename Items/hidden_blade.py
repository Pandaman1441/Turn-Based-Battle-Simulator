from Items.item_class import Item




class Hidden_Blade(Item):
    def __init__(self):
       super().__init__(name = "Hidden Blade",
        stats = {
            "ag": 50
        },
        description = "test.",
        cost = 1450,
        build = ["Initiate's Dagger", "Flowing Cloak"],
        icon = "Assets/item_icons/tile084.png")
 