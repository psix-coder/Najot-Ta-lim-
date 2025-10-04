class city:
    def __init__(self, nomi, aholisi, joylashuvi, tabiati,):

        self.nomi = nomi
        self.aholisi = aholisi
        self.joylashuvi = joylashuvi
        self.tabiat = tabiati

    def __str__(self):
        return (f"Shahar nomi: {self.nomi},\n"
        f"Aholisi: {self.aholisi},\n"
        f"Joylashuvi: {self.joylashuvi},\n"
        f"Tabiati: {self.tabiat}")
    
ciity = city("Farg'ona", "5 million", "O'zbekiston", "Suptropic")

print(ciity)