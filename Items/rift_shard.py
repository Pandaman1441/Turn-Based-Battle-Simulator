from Items.item_class import Item




class Rift_Shard(Item):
    def __init__(self):
        super().__init__(name = "Rift Shard",
        stats = {
            "mp": 75
        },
        description = "test.",
        cost = 1400,
        build = ["Mystic Tome", "Arcane Focus"],
        icon = "Assets/item_icons/general/tile011.png")
