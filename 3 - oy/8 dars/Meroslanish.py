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
    


class User:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    def tanishtir(self):
        return f"Mening Ismim {self.f_name}, Familyam {self.l_name}"
    
class Techer:
    def __init__(self, f_name, l_name, fan):
        User.__init__(f_name, l_name)
        self.fan = fan

class Student:
    def __init__(self, f_name, l_name, Universitet):
        User.__init__(f_name, l_name)
        self.Universitet = Universitet




class A:
    def __init__(self, a):
        self.a = a
        
    def tanishtir(self):
        return f"Men A class man "


class B:
    def __init__(self, b):
        self.b = b

    def tanishtir(self):
        return f"Men B class man "


class C:
    def __init__(self, c):
        self.c = c

    def tanishtir(self):
        return f"Men C class man "



class D(A,B,C):
    def __init__(self, a,b,c):
        A.__init__(self, a)
        B.__init__(self, b)
        C.__init__(self, c)



# print("salom")