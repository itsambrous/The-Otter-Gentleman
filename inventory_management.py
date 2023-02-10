# Creating Inventory 

class Inventory:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.quantity = quantity

inventory = []

def add_item(item_name, quantity):
    new_item = Inventory(item_name, quantity)
    inventory.append(new_item)

def update_item(item_name, quantity):
    for item in inventory:
        if item.item_name == item_name:
            item.quantity = quantity

def report():
    for item in inventory:
        print("Item: {}\tQuantity: {}".format(item.item_name, item.quantity))

# Example usage
add_item("apple", 10)
add_item("banana", 5)

print("Original inventory:")
report()

update_item("banana", 10)

print("\nUpdated inventory:")
report()
