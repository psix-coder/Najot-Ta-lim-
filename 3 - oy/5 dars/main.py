class Product:
    objects = []
    def __init__(self, nomi, narx,  soni, discount = None):

        self.nomi = nomi
        self.name = narx
        self.soni = soni
        self.discount = None
        Product.objects+=[self]
