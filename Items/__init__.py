import os
import importlib
from pathlib import Path
from Items.item_class import Item



def load_all_items():
    shop_items = {}

    base = Path(__file__).parent
    for file in os.listdir(base):
        if file.endswith(".py") and file not in {"__init__.py", "item_class.py"}:
            module_name = f"{__name__}.{file[:-3]}"
            module = importlib.import_module(module_name)
            for attr in dir(module):
                obj = getattr(module, attr)   
                if isinstance(obj, type) and issubclass(obj, Item) and obj is not Item:
                    instance = obj()  # Create the item instance
                    shop_items[instance.name] = instance
    return shop_items        