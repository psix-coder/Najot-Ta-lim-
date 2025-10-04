class Davlat:
    def __init__(self, Nomi, Aholisi, Tabiati, Joylashuvi, Pul_birligi):

        self.nomi = Nomi
        self.Aholisi = Aholisi
        self.Tabiati = Tabiati
        self.Joylashuvi = Joylashuvi
        self.Pul_birligi = Pul_birligi

    def __str__(self):
        return (f"Davlat nomi: {self.nomi},\n"
                f"Aholisi: {self.Aholisi},\n"
                f"Tabiati: {self.Tabiati},\n"
                f"Joylashuvi: {self.Joylashuvi},\n"
                f"Pul birligi: {self.Pul_birligi},\n"
                )
    
davlaaat = Davlat("O'zbekiston", "40 000 million", "Suptropic", "Markaziy osiyo", "So'm")
print(davlaaat)