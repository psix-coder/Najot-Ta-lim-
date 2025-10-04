class Product:
    products = [] 

    def init(self, name, price, quantity, discount=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.discount = discount
        Product.products.append(self)  

    @staticmethod
    def discount_products():
        results = []
        for product in Product.products:  
            if product.discount:
                results.append(product)        @staticmethod
    def max_price_products():
        return max(Product.products, key=lambda x: x.price)
    
    @staticmethod
    def min_price_products():
        return min(Product.products, key=lambda x: x.price)
        return results
