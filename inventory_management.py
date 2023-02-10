# Creating Inventory 

class Inventory:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

inventory = []

def add_item(item_name, quantity, price):
    new_item = Inventory(item_name, quantity, price)
    inventory.append(new_item)

def update_item(item_name, quantity, price):
    for item in inventory:
        if item.item_name == item_name:
            item.quantity = quantity
            item.price = price

def report():
    for item in inventory:
        print("Item: {}\tQuantity: {}\tPrice: {:.2f} €".format(item.item_name, item.quantity, item.price))

# Example usage
add_item("oranges", 10, 0.5)
add_item("banana", 5, 0.3)

print("Original inventory:")
report()

update_item("banana", 10, 0.4)

print("\nUpdated inventory:")
report()
