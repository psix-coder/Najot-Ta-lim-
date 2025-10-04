class car:
    def __init__(self, model, kompanya, rang, narx, tezlik ):
        
        self.model = model
        self.kompanya = kompanya
        self.rang = rang
        self.narx = narx
        self.tezlik = tezlik

    def __str__(self):
        return (f"Model: {self.model},\n"
        f"Kompanya: {self.kompanya},\n"
        f"Rang: {self.rang},\n"
        f"Narx: {self.narx},\n"
        f"tezlik: {self.tezlik}"
        )
    
caar = car("BMW M4 E60", "BMW", "Ko'k", 150_000, "400 km")

print(caar)

