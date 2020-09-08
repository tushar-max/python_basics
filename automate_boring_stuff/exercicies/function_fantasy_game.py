
def addToInventory(inventory, addedItems):
    """
    Add the items to the dictionary
    """
    # added items é uma lista
    # passar pelos elementos da lista de cada e adiciona los ao dictionary
    # usar setdefault para casa ja exista no dicionario acrescentar e caso nao exista fica igual ao valor
    for items in addedItems:
        # if element not in the dictionary
        inventory.setdefault(items, 0)
        # When the element is in the dictionary
        inventory[items] += 1 



    return inventory


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

inventory = addToInventory(inventory, dragonLoot)

print(inventory)