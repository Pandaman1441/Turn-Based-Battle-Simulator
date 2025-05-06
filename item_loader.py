



def load_items(items):
    from Items import item_registry

    item_objects = []
    for item in items:
        if item in item_registry:
            item_obj = item_registry[skill]   # Gets a object
            item_objects.append(item_obj())
        else:
            print("item name wrong")
    return item_objects