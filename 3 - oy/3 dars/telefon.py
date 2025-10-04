class Telefon:
    def __init__(self, model, kompanya, yil, rang, narxi, xotirasi, qoshimcha_xotira, Batareya_xolati,):

        self.model = model
        self.kompanya = kompanya
        self.yil = yil
        self.rang = rang
        self.narxi = narxi
        self.xotirasi = xotirasi
        self.qoshimcha_xotira = qoshimcha_xotira
        self.Batareya_xolati = Batareya_xolati

    def __str__(self):
        return (f"Telefon modeli: {self.model},\n"
                f"Kompanya nomi: {self.kompanya},\n"
                f"Telefon ishlab chiqarilgan sana: {self.yil},\n"
                f"Rangi: {self.rang},\n"
                f"Narxi: {self.narxi},\n"
                f"Telefon xotirasi: {self.xotirasi},\n"
                f"Tezkor xotira: {self.qoshimcha_xotira},\n"
                f"Batareya xolati: {self.Batareya_xolati},\n"
                )

tf = Telefon("iPhone", "Apple", 2024, "Oq", "1500 $", "1 tr", 32, 99)

print(tf )