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
        print("Product list:")
        for product in self.list_products:
            print(f"{product.name}")
        
    def remove_product(self, product):
        for p in self.list_products:
            if p.name == product:
                self.list_products.remove(p)
                self.total_price -= p.price
                break