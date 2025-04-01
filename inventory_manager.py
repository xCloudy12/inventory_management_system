

class InventoryManager:
    
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, price, quantity):
        self.inventory[name] = {"price": price, "quantity": quantity}

    def get_product_info(self, name):
        return self.inventory.get(name, "Product not found")

    def get_total_inventory_value(self):
        return sum(item["price"] * item["quantity"] for item in self.inventory.values())
