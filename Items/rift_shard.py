from Items.item_class import Item




class Rift_Shard(Item):
    def __init__(self):
        super().__init__(name = "Rift Shard",
        stats = {
            "mp": 40
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/general/tile011.png")
