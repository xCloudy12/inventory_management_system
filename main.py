from inventory.inventory_manager import InventoryManager
from inventory.product import Product

def display_menu():
    """Display the main menu options."""
    print("\n=== INVENTORY MANAGEMENT SYSTEM ===")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. List All Products")
    print("6. Check Low Stock")
    print("7. Total Inventory ")
    print("8. Exit")

def add_product(inventory):
    """Handle adding a new product."""
    print("\n--- ADD NEW PRODUCT ---")
    name = input("Product Name: ").strip()
    
    # Check if product already exists
    if inventory.get_product_info(name) != f"Product '{name}' not found":
        print(f" Product '{name}' already exists!")
        return
    
    try:
        price = float(input("Price (€): "))
        quantity = int(input("Quantity: "))
        inventory.add_product(Product(name, price, quantity))
        print(f" '{name}' added successfully!")
    except ValueError as e:
        print(f" Error: {e}")

def search_product(inventory):
    """Handle product search."""
    print("\n--- SEARCH PRODUCT ---")
    name = input("Enter product name: ").strip()
    print(inventory.get_product_info(name))

def update_product(inventory):
    """Product updates."""
    print("\n--- UPDATE PRODUCT ---")
    name = input("Product name to update: ").strip()
    
    if inventory.get_product_info(name) == f"Product '{name}' not found":
        print(f" Product '{name}' not found!")
        return
    
    print("\nWhat do you want to update?")
    print("1. Price")
    print("2. Quantity")
    choice = input("Choice (1-2): ")
    
    try:
        if choice == "1":
            new_price = float(input("New price (€): "))
            inventory.inventory[name].update_price(new_price)
        elif choice == "2":
            new_qty = int(input("New quantity: "))
            inventory.update_product_quantity(name, new_qty)

        else:
            print(" Invalid choice")
            return
        print(f" '{name}' updated successfully!")
    except ValueError as e:
        print(f" Error: {e}")

def delete_product(inventory):
    """Product delete."""
    print("\n--- DELETE PRODUCT ---")
    name = input("Enter product name to delete: ").strip()
    try:
        inventory.remove_product(name)
        print(f" '{name}' deleted successfully!")
    except KeyError:
        print(f" Product '{name}' not found!")

def list_products(inventory):
    """List all products."""
    print("\n--- ALL PRODUCTS ---")
    if not inventory.inventory:
        print("No products in inventory")
        return
    
    for product in inventory.inventory.values():
        print(product.get_product_info())

def check_low_stock(inventory):
    """Check low stock items."""
    print("\n--- LOW STOCK  ---")
    threshold = int(input("Enter threshold quantity (default 5): ") or 5)
    low_stock = inventory.get_low_stock_products(threshold)
    
    if not low_stock:
        print(f"No products below {threshold} units")
    else:
        for product in low_stock:
            print(f" {product.get_product_info()}")

def main():
    inventory = InventoryManager()
    
    
    while True:
        display_menu()
        choice = input("Enter choice (1-8): ")
        
        if choice == "1":
            add_product(inventory)
        elif choice == "2":
            search_product(inventory)
        elif choice == "3":
            update_product(inventory)
        elif choice == "4":
            delete_product(inventory)
        elif choice == "5":
            list_products(inventory)
        elif choice == "6":
            check_low_stock(inventory)
        elif choice == "7":
            print(f"\nTotal Inventory Value: Є{inventory.get_total_inventory_value():.2f}")
        elif choice == "8":
            print("Arrivederci")
            break
        else:
            print(" Invalid choice. Please enter 1-8")

if __name__ == "__main__":
    main()