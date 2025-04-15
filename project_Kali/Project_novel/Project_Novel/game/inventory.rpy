default inventory = []

python:
    def add_item(item):
        if item not in inventory:
            inventory.append(item)

    def remove_item(item):
        if item in inventory:
            inventory.remove(item)
