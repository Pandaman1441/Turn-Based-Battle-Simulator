from Items.item_class import Item




class Hidden_Blade(Item):
    def __init__(self):
       super().__init__(name = "Hidden Blade",
        stats = {
            "ag": 40
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/tile084.png")
