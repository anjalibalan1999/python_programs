# Dictionary to hold the inventory items
inventory = {}

def add_item(name, quantity, price):
    """Add a new item to the inventory."""
    if name in inventory:
        print(f"Item '{name}' already exists in the inventory.")
    else:
        inventory[name] = {"quantity": quantity, "price": price}
        print(f"Item '{name}' added to the inventory.")

def remove_item(name):
    """Remove an item from the inventory."""
    if name in inventory:
        del inventory[name]
        print(f"Item '{name}' removed from the inventory.")
    else:
        print(f"Item '{name}' does not exist in the inventory.")

def update_quantity(name, quantity):
    """Update the quantity of an existing item."""
    if name in inventory:
        inventory[name]["quantity"] = quantity
        print(f"Quantity of item '{name}' updated to {quantity}.")
    else:
        print(f"Item '{name}' does not exist in the inventory.")

def calculate_total_value():
    """Calculate the total value of the inventory."""
    total_value = sum(item["quantity"] * item["price"] for item in inventory.values())
    return total_value

# Example usage
add_item("Apple", 50, 0.5)          # Add 50 apples with a price of $0.5 each
add_item("Banana", 100, 0.3)        # Add 100 bananas with a price of $0.3 each
add_item("Orange", 75, 0.6)         # Add 75 oranges with a price of $0.6 each

print("\nInventory after adding items:")
print(inventory)

remove_item("Banana")               # Remove bananas from the inventory

print("\nInventory after removing bananas:")
print(inventory)

update_quantity("Apple", 60)        # Update the quantity of apples to 60

print("\nInventory after updating quantity of apples:")
print(inventory)

total_value = calculate_total_value() # Calculate the total value of the inventory
print(f"\nTotal value of the inventory: ${total_value:.2f}")
