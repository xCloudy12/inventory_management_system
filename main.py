
# main.py

from inventory_manager import InventoryManager

def main():
    inventory =  InventoryManager()
    
    inventory.add_product("iPad", 1200, 3)
    inventory.add_product("iPhone", 1100, 5)
    inventory.add_product("Airpods", 250, 10)
    
    print("Inventory Details:")
    print(inventory.get_product_info("iPad"))
    print(inventory.get_product_info("iPhone"))
    print(inventory.get_product_info("Airpods"))
    
    total_value = inventory.get_total_inventory_value()
    print("Total Inventory Value:", total_value)

if __name__ == "__main__":
    main()

