class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __eq__(self, other):                        
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price
    
    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price
    
    def __le__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price <= other.price
    
    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price
    
    def __ge__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price >= other.price