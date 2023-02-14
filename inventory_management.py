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
add_item("Silk Ties", 80, 95)
add_item("Bow-Ties", 100, 60)

print("Original inventory:")
report()

update_item("Silk Ties", 75, 90)

print("\nUpdated inventory:")
report()
