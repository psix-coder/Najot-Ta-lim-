class Product:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi
    
    def __eq__(self, boshqa):
        if isinstance(boshqa, Product):
            return self.narxi == boshqa.narxi
        return False
    
    def __lt__(self, boshqa):
        if isinstance(boshqa, Product):
            return self.narxi < boshqa.narxi
        return NotImplemented
    
    def __gt__(self, boshqa):
        if isinstance(boshqa, Product):
            return self.narxi > boshqa.narxi
        return NotImplemented
                            
    def __le__(self, boshqa):
        if isinstance(boshqa, Product):
            return self.narxi <= boshqa.narxi
        return NotImplemented
    
    def __ge__(self, boshqa):
        if isinstance(boshqa, Product):
            return self.narxi >= boshqa.narxi
        return NotImplemented

