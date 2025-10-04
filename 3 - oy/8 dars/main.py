class Product:
    def __init__(self, name, price, ):
        self.name = name
        self.price = price
       
class Category:         
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Faqat Product turidagi obyektlar qo'shilishi mumkin")

    def filter_by_price_range(self, min_price, max_price):
        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_by_name(self, keyword):
        return [product for product in self.products if keyword.lower() in product.name.lower()]

    def filter_by_price_less_than(self, price):
        return [product for product in self.products if product.price < price]

    def filter_by_price_greater_than(self, price):
        return [product for product in self.products if product.price > price]

    def sort_products_by_price(self, reverse=False):
        return sorted(self.products, key=lambda x: x.price, reverse=reverse)
    
    

