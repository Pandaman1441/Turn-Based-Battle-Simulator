from Items.item_class import Item




class Hexed_Maul(Item):
    def __init__(self):
        super().__init__(name = "Hexed Maul",
        stats = {
            "pp": 20,
            "mr": 20
        },
        description = "test.",
        cost = 950,
        build = ["Recruit's Sword", "Anti-Magic Cloak"],
        icon = "Assests/item_icons/tile030.png")
