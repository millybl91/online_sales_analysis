class Product():
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        print(f"Product: {self.name}, has a price: {self.price}, available quantity: {self.quantity}")
    
    def update_quantity(self, change_quantity: int):
        self.quantity = change_quantity
        return self.quantity

