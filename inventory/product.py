class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_info(self):
        return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def get_value(self):
        return self.price * self.quantity

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_product(self, name, price, quantity):
        if name in self.inventory:
            self.inventory[name].quantity += quantity 
        else:
            self.inventory[name] = Product(name, price, quantity)

    def remove_product(self, name):
        if name in self.inventory:
            del self.inventory[name]
        else:
            print("Product not found in inventory.")

    def update_quantity(self, name, quantity):
        if name in self.inventory:
            self.inventory[name].quantity = quantity
        else:
            print("Product not found in inventory.")

    def get_product_info(self, name):
        if name in self.inventory:
            return self.inventory[name].get_info()
        else:
            return "Product not found"

    def get_total_inventory_value(self):
        return sum(product.get_value() for product in self.inventory.values())

inventory = InventoryManager()
inventory.add_product("Laptop", 1000, 5)
inventory.add_product("Mouse", 50, 10)
print(inventory.get_product_info("Laptop"))  # Product: Laptop, Price: 1000, Quantity: 5
print("Total Inventory Value:", inventory.get_total_inventory_value()) 
