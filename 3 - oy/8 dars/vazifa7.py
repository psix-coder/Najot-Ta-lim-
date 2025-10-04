class Category:
    def __init__(self, name):
        self.name = name
        self.products = []

    def __str__(self):
        return self.name
    
    def filter(self, price_lte):
        return tuple(filter(lambda x:x<= price_lte, self.products))
    
class Product:
    def __init__(self, name:str, category:Category, price:float):
        self.name:str = name
        self.category:Category = category
        self.category.products.append(self)
        self.price = price

    def __str__(self):
        return self.name
    

class user:
    def __init__(self, nomi, narxi, soni, kupon ):
        self.nomi = nomi
        self.narxi = narxi
        self.soni = soni 
        self.kupon = kupon 

    def __str__(self):
        return self.nomi
    

    def __add__(self, name, nom):
        self.name = name
        self.nom = nom 





