from inventory.inventory_manager import InventoryManager
from inventory.product import Product

def main():
   
    # Initialize inventory manager
    inventory = InventoryManager()
    
    # Add some sample products
    try:
        inventory.add_product(Product("Notebook", 900, 10))
        inventory.add_product(Product("Mouse", 24.99, 30))
        inventory.add_product(Product("PC", 1500, 50))
        inventory.add_product(Product("Playstation", 500, 100))
        inventory.add_product(Product("TV", 1500, 15))
    except ValueError as e:
        print(f"Error adding product: {e}")
    
    # Display product information
    print("\nProduct Information:")
    print(inventory.get_product_info("Notebook"))
    print(inventory.get_product_info("Mouse"))
    print(inventory.get_product_info("PC"))
    print(inventory.get_product_info("Playstation"))
    print(inventory.get_product_info("TV"))   
    
    print(inventory.get_product_info("Product not exist"))
    
    
    # Get low stock products
    print("\nLow Stock (quantity < 20):")
    for product in inventory.get_low_stock_products(20):
        print(f"- {product.get_product_info()}")
    
    # Calculate total inventory value
    total_value = inventory.get_total_inventory_value()
    print(f"\nTotal Inventory Value: {total_value:.2f} Є")
    

if __name__ == "__main__":
    main()