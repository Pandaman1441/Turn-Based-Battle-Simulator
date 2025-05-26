from abc import ABC


class Item(ABC):
    def __init__(self, name="Item", stats=None, description="", cost=0, build=None, icon="Assets/item_icons/placeholder.png"):
        self._name = name
        self._stats = stats if stats else {}
        self._description = description
        self._cost = cost
        self._build = build if build else []
        self._icon = icon

    @property
    def stats(self):
        return self._stats
    
    @property
    def cost(self):
        return self._cost
    
    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
    
    @property
    def build(self):
        return self._build

    @property
    def icon(self):
        return self._icon