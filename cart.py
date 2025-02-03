from product import Product
from product__manager import ProductManager

class Cart(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

# Mali komentar:
# Nisam ispisivao metode u cart.py jer sam ih vec ispisao u product_manager.py.
# Nije mi imalo smilsa da ih ponavlja kad sam vec sve sto mi treba ispisao u prethondom primjeru.
# Tako da je i ovaj cart suviras ali cu ga ostaviti u skopu zadatka.
