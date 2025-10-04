# 1 Topshiriq

# a = ["olma", "banan", 'non', 'sut']
# b = ('tuxum', 'yog')

# a.extend(b)

# print(a)

# 2 Topshiriq

# sonlar = [3, 7, 2, 9, 100, 120, 18, 7]

# sonlar1 = max(sonlar)
# sonlar2 = min(sonlar)

# print(f'Eng katta son: {sonlar1}')
# print(f'Eng kichik son: {sonlar2}')

# 3 Topshiriq

# buyurtmalar = [
#     "Abdulloh Ahmadjonov: 3 ta BMW",
#     "Muhammadjon Abdujabborov: 2 ta Orlando",
#     "Jamoliddin Xolmatov: 1 ta Tesla",
#     "Davron Nazarov: 5 ta Porshe"
# ]

# xaridor = input("Xaridor ism, familyasin kiriting: ")

# found = False  
# for buyurtma in buyurtmalar:
#     if buyurtma.startswith(xaridor):
#         print(f"{xaridor}ning buyurtmasi: {buyurtma.split(': ')[1]}")   
#         found = True
#         break

# if not found:
#     print(f"{xaridor} uchun buyurtma topilmadi.")

# # (Split  ':' ) bu kiritilgan malumotni ikkiga ajratadi. 1 bu malumotni birinchi qismini ol degani!


# 4 Topsjiriq 
# Juft
# num = [num for num in range(1, 101) if num % 2 == 0]
# print(num)

# Toq
# num = [num for num in range(1, 101) if num % 2 != 0]
# print(num)

# Codda list ichida tsikl aylantirilgan qisqa va lo'nda 

# 5 Topshiriq
# def tartibla_va_ortacha(royxat):
#     tartiblangan = sorted(royxat)
#     uzunlik = len(tartiblangan)         
    
#     if uzunlik % 2 == 1:
#         ortacha = tartiblangan[uzunlik // 2]
#     else:
#         ortacha = (tartiblangan[uzunlik // 2 - 1] + tartiblangan[uzunlik // 2]) / 2
    
#     return tartiblangan, ortacha

# misol_royxat = [5, 2, 9, 1, 6, 1, 43,  6, 56, 3, 453, 42,]

# tartiblangan, ortacha_qiymat = tartibla_va_ortacha(misol_royxat)

# print(f"Tartiblangan ro'yxat: {tartiblangan}")
# print(f"O'rtacha qiymat: {ortacha_qiymat}")

