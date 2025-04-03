class Product:
    
    def __init__(self, name: str, price: float, quantity: int):

        self.name = name
        self.price = price
        self.quantity = quantity
        
    def update_quantity(self, new_quantity: int) -> None:

        if new_quantity >= 0:
            self.quantity = new_quantity
        else:
            raise ValueError("Quantity must be positive")
    
    def update_price(self, new_price: float) -> None:

        if new_price >= 0:
            self.price = new_price
        else:
            raise ValueError("Price must be positive")
    
    def get_product_info(self) -> str:

        return (f"Product: {self.name}, Price: {self.price:.2f} Є, "
                f"Quantity: {self.quantity}")
    
    def get_total_value(self) -> float:

        return self.price * self.quantity