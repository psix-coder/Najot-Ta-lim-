mashina = []

print("Avtomobillarni ro'yxatini kiriting. Dasturni tugatish uchun 'stop' ni kiriting.")

while True:
    avto_nom = input("Avtomobil nomi: ")
    if avto_nom.lower() == 'stop':
        break
    mashina.append(avto_nom)

avto_dict = {}
for index, avto in enumerate(mashina):
    avto_dict[avto] = index + 1

print("Avtomobillar ro'yxati:", mashina)
print("Dictionary natijasi:", avto_dict)