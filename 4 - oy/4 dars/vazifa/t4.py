from collections import namedtuple

Avto = namedtuple("Avto",["make", "model", "year"])

avto1 = Avto(make = "BMW", model = "M8", year = 2024)
avto2 = Avto(make = "Porshe", model = "911", year = 2018)
avto3 = Avto(make = "Gentra", model = "3", year = 2020)

avtomabillar = [avto1, avto2, avto3]

eng_yangi = max(avtomabillar, key=lambda avto: avto.year)

print(f"Eng yangi avtomabil: {eng_yangi.make}      Modeli: {eng_yangi.model}      Ishlab chiqarilgan yili:  {eng_yangi.year}")



