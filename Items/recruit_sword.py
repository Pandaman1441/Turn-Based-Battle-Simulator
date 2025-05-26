from Items.item_class import Item




class Recruit_Sword(Item):
    def __init__(self):
        super().__init__(name = "Recruit's Sword",
        stats = {
            "pp" : 10
        },
        description = "test.",
        cost = 300,
        build = [],
        icon = "Assests/item_icons/tile014.png"
)