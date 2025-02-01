from product import Product
from product__manager import ProductManager 

def main():
    pm = ProductManager("", 0, 0)
    pm1 = ProductManager("Dzemper", 500, 13)
    pm2 = ProductManager("Patike", 800, 32)
    pm3 = ProductManager("Cipele", 750, 14)
    pm4 = ProductManager("Jakna", 630, 22)

    pm.add_product(pm1.name)
    pm.add_product(pm2.name)
    pm.add_product(pm3.name)
    pm.add_product(pm4.name)

    pm.product_info_list()

    pm.update_total_price(pm1.price)
    pm.update_total_price(pm2.price)
    pm.update_total_price(pm3.price)
    pm.update_total_price(pm4.price)
    print(f"Total product price from the list: {pm.total_price}")
    
if __name__ == "__main__":
    main()









"""pm.add_product(p.name)
print(pm.add_price(300))
pm.product_info_list()
pm.update_total_price(300)
pm.update_total_price(100)
pm.update_total_price(200)
print(pm.total_price)"""