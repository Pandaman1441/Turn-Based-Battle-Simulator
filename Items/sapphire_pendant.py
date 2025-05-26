from Items.item_class import Item




class Sapphire_Pendant(Item):
    def __init__(self):
        super().__init__(name = "Sapphire Pendant",
        stats = {
            "mp": 25,
            "wp": 25
        },
        description = "test.",
        cost = 1,
        build = [],
        icon = "Assests/item_icons/general/tile046.png")
