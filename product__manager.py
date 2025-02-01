from product import Product


class ProductManager(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.list_products = []
        self.total_price = 0
        
    def add_product(self,new_product):
        self.list_products.append(new_product)
    
    def update_total_price(self, new_price):
        self.total_price += new_price
        return self.total_price
        
    def product_info_list(self):
        print(f"Product list: {self.list_products}")
        
