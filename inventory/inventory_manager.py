from typing import Dict, List
from .product import Product

class InventoryManager:

    
    def __init__(self):
   
        self.inventory: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> None:

        if product.name in self.inventory:
            raise ValueError(f"Product '{product.name}' Product already exists")
        self.inventory[product.name] = product
    
    def remove_product(self, product_name: str) -> None:

        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' Product not found")
        del self.inventory[product_name]
    
    def update_product_quantity(self, product_name: str, new_quantity: int) -> None:

        if product_name not in self.inventory:
            raise KeyError(f"Product '{product_name}' Product not found")
        self.inventory[product_name].update_quantity(new_quantity)
    
    def get_product_info(self, product_name: str) -> str:

        product = self.inventory.get(product_name)
        return product.get_product_info() if product else f"Product '{product_name}' not found"
    
    def get_total_inventory_value(self) -> float:

        return sum(product.get_total_value() for product in self.inventory.values())
    
    def get_products_by_category(self, category: str) -> List[Product]:

        return [product for product in self.inventory.values() 
                if product.category and product.category.lower() == category.lower()]
    
    def get_low_stock_products(self, threshold: int = 5) -> List[Product]:

        return [product for product in self.inventory.values() 
                if product.quantity < threshold]