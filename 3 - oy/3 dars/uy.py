class Uy:
    def __init__(self, narxi, joylashuvi, yili, sharoitti,):
        self.narxi = narxi
        self.joylashuvi = joylashuvi
        self.yili = yili
        self.sharoiti = sharoitti

    def __str__(self):
        return (f"Uy narxi: {self.narxi},\n"
                f"JOyalashuvi: {self.joylashuvi},\n"
                f"Yili: {self.yili},\n"
                f"Sahroiti: {self.sharoiti}"
                )
    
uyy = Uy("150000 $", "Dubai", "2024", "Comfort")

print(uyy)

