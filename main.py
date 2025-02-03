from product import Product
from product__manager import ProductManager 
from cart import Cart
import random

def main():
    pm = ProductManager("", 0, 0)
    pm1 = ProductManager("Dzemper", 500, 13)
    pm2 = ProductManager("Patike", 800, 32)
    pm3 = ProductManager("Cipele", 750, 14)
    pm4 = ProductManager("Jakna", 630, 22)
    pm5 = ProductManager("Kosulja", 200, 20)
    pm6 = ProductManager("Sesir", 300, 17)
    
    pm.add_product(pm1)
    pm.add_product(pm2)
    pm.add_product(pm3)
    pm.add_product(pm4)
    pm.add_product(pm5)
    pm.add_product(pm6)
    
    pm.product_info_list()

    pm.update_total_price(pm1.price, pm1.quantity)
    pm.update_total_price(pm2.price, pm2.quantity)
    pm.update_total_price(pm3.price, pm3.quantity)
    pm.update_total_price(pm4.price, pm4.quantity)
    pm.update_total_price(pm5.price, pm5.quantity)
    pm.update_total_price(pm6.price, pm6.quantity)
    
    print(f"Total product price from the list with quantity available: {pm.total_price}")
    print()
    
    pm.remove_product("Jakna")
    pm.product_info_list()
    print(f"Total product price from the list with quantity available: {pm.total_price}")
    print()
    
    c = random.sample(pm.list_products, 3)
    price = 0
    for customer in c:
        customer_quantity = random.randint(1, 10)
        customer.update_quantity(customer_quantity)
        customer.product_info()
        customer.update_total_price(customer.price, customer.quantity)
        price += customer.total_price
    print(f"Total product price for the customer: {price}")
    
    
if __name__ == "__main__":
    main()




