



def load_items(items):
    import Items
    full_list = Items.load_all_items()
    item_objects = []
    for item in items:
        if item in full_list:
            item_obj = full_list[item]   # Gets a object
            item_objects.append(item_obj)
        else:
            print("item name wrong")
    return item_objects