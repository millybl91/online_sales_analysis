# online_sales_analysis
Final project

Rad sa proizvodima(dodavanje, prikaz, azuriranje, uklanjanje):

1. Kreiranje datoteke produkt.py sa klasom Product i metodama product_info i update_quantity
    - metoda product info ispisuje atribute klase Product zadatog proizvoda
    - metoda update_quantity mjenja kolicinu zadatog proizvoda

2. Kreiranje datotke product_manager.py sa klasom ProductManager i metodama add_product, update_total_price, product_info_list, remove_product
    - Klasa ProductManager nasljedjuje atribute klase Produkt
    - add_product dodaje citav objekat koji smo zadali u listu self.list_products
    - update_total_price izracunava ukupnu vrijednost proizvoda koji su na stanju zajedno sa kolicinom proizvoda
    - product_info_list ispisu imena proizvoda na stanju
    - remove_product uklanjamo proizvod koji zelimo da obrisemo

3. Kreiranje cart.py, nisu kreirane nikakve izmjene samo dokumentovano zasto je je tako

4. Kreiranje main.py, upisivanje svih objekata i pozivanje metoda za njihovo izvrsavanje

