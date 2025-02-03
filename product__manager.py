from product import Product

class ProductManager(Product):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.list_products = []
        self.total_price = 0
        
    def add_product(self,new_product: object):
        self.list_products.append(new_product)
    
    def update_total_price(self, new_price: float, new_quantity: int):
        self.total_price += new_price * new_quantity
        return self.total_price
        
    def product_info_list(self):
        print("Product list:")
        for product in self.list_products:
            print(f"{product.name}")
        
    def remove_product(self, product: str):
        for p in self.list_products:
            if p.name == product:
                self.list_products.remove(p)
                self.total_price -= p.price * p.quantity
                break