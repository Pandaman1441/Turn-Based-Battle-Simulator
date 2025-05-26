from Items.item_class import Item




class Bone_Necklace(Item):
    def __init__(self):
        super().__init__(
            name = "Bone Necklace",
            stats = {
                "wp": 20
            },
            description = "test.",
            cost = 350  ,
            build = [],
            icon = "Assests/item_icons/misc/tile001.png"
    )