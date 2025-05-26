from Items.item_class import Item




class Anti_Magic_Cloak(Item):
    def __init__(self):
        super().__init__(
            name = "Anti-Magic Cloak",
            stats = {
                "mr": 20
            },
            description = "test.",
            cost = 350,
            build = [],
            icon = "Assests/item_icons/tile074.png"
        )
