from Items.item_class import Item




class Arcatech_Codex(Item):
    def __init__(self):
        super().__init__(
        name = "Arcatech Codex",
        stats = {
            "mp": 20,
            "pr": 25
        },
        description = "test.",
        cost = 1150,
        build = ["Mystic Tome", "Buckler"],
        icon = "Assets/item_icons/tile026.png"
)
   