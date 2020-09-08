def displayInventory(inventory):
    """
    keys are string values describing the item in the inventory
    value is an integer value detailing how many of that item the player has

    Example:
    {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

    """
    print("Inventory:")
    number_items = 0
    for key, value in inventory.items():
        print("%s %s" % (value, key))
        number_items += value
    
    print("Total number of items: %s" % number_items)


displayInventory({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})
