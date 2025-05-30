from Items.item_class import Item




class Verdant_Boots(Item):
    def __init__(self):
        super().__init__(name = "Verdant Boots",
        stats = {
            "r": 350,
            "ag": 20,
        },
        description = "test.",
        cost = 950,
        build = ["Mana Crystal", "Initiate's Dagger"],
        icon = "Assests/item_icons/misc/tile005.png"
)