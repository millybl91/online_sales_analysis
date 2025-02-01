from product import Product
from product__manager import ProductManager 

def main():
    pm = ProductManager("", 0, 0)
    pm1 = ProductManager("Dzemper", 500, 13)
    pm2 = ProductManager("Patike", 800, 32)
    pm3 = ProductManager("Cipele", 750, 14)
    pm4 = ProductManager("Jakna", 630, 22)

    pm.add_product(pm1)
    pm.add_product(pm2)
    pm.add_product(pm3)
    pm.add_product(pm4)

    pm.product_info_list()

    pm.update_total_price(pm1.price)
    pm.update_total_price(pm2.price)
    pm.update_total_price(pm3.price)
    pm.update_total_price(pm4.price)
    print(f"Total product price from the list: {pm.total_price}")
    print()
    
    pm.remove_product("Jakna")
    pm.product_info_list()
    print(f"Total product price from the list: {pm.total_price}")

    
    
    
if __name__ == "__main__":
    main()



