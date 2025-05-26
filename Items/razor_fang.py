from Items.item_class import Item




class Razor_Fang(Item):
    def __init__(self):
        super().__init__(name = "Razor Fang",
        stats = {
            "crit_chance": 5
        },
        description = "test.",
        cost = 250,
        build = [],
        icon = "Assests/item_icons/general/tile002.png"
)