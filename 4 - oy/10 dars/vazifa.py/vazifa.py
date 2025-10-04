# 1 misol 

# def son_hisobla(son):
#     total = 0
#     i = 0

#     while i < len(son):
#         total += son[i]
#         i += 1

#     return total

# son = [1,2,3,4,5,6,7,8,9,10]
# print("Yig'indi: ", son_hisobla(son))

# 2 misol

# def aylantir(son):
#     return son[1:] + son[:1]

# sonlar = [1,2,3,4]
# print(aylantir(sonlar))


# 3 misol

# def sonni_top(son):
#     max_son = max(son)
#     min_son = min(son)

#     return max_son, min_son

# numbers = [1,2,3,4,5,20,30,40,50]
# eng_katta, eng_kichik = sonni_top(numbers)

# print("Eng katta son:", eng_katta)
# print("Eng kichik son:", eng_kichik)


# 4 misol 

# def qiymat_tekshi(royxat, qiymat):
#     if qiymat in royxat:
#         return f"{qiymat} ro'yxatda mavjud!"
#     else:
#         return f"{qiymat} ro'yxatda mavjud emas!"
    
# numbers = [1,2,3,4,5,6,7,8,9,10]

# qiymat = int(input("Qidirilayotgan sonni kiriting: "))
# print(qiymat_tekshi(numbers, qiymat))


# 5 misol 

# def unikal_elementlar(royxat):
#     return list(set(royxat))

# numbers = [1, 2, 3, 4, 2, 5, 1, 6, 4]
# unikal_royxat = unikal_elementlar(numbers)

# print("Unikal elementlar ro'yxati:", unikal_royxat)


# 6 misol 

# def sozlarni_teskari_aylantir(royxat):
#     return [soz[::-1] for soz in royxat]

# sozlar = ["salom", "dunyo", "python", "dasturlash"]
# teskari_sozlar = sozlarni_teskari_aylantir(sozlar)

# print("Teskari aylangan so'zlar:", teskari_sozlar)


# 7 misol 

# def eng_uzun_soz(royxat):
#     eng_uzun = max(royxat, key=len)
#     return eng_uzun

# sozlar = ["salom", "dunyo", "python", "dasturlash"]
# uzun_soz = eng_uzun_soz(sozlar)

# print("Eng uzun so'z:", uzun_soz)


#  8 misol 

# def takrorlangan_qiymatlar_top(lugat):
#     qiymatlar = list(lugat.values())
#     takrorlangan = set([qiymat for qiymat in qiymatlar if qiymatlar.count(qiymat) > 1])
#     return takrorlangan

# lugat = {
#     "A": 1,
#     "B": 2,
#     "C": 3,
#     "D": 2,
#     "E": 4,
#     "F": 3
# }

# takrorlangan_qiymatlar = takrorlangan_qiymatlar_top(lugat)
# print("Takrorlangan qiymatlar:", takrorlangan_qiymatlar)



#  9 misol

# def raqamlarni_top_va_sarala(lugat):
#     raqamlar = [qiymat for qiymat in lugat.values() if isinstance(qiymat, (int, float))]
#     raqamlar.sort()
#     return raqamlar

# lugat = {
#     "A": 10,
#     "B": 5.5,
#     "C": "salom",
#     "D": 20,
#     "E": 3,
#     "F": "dunyo"
# }

# saralangan_raqamlar = raqamlarni_top_va_sarala(lugat)
# print("Saralangan raqamlar:", saralangan_raqamlar)



# 10 misol

# def raqamlarni_ikki_barobar_kopaytir(lugat):
#     for kalit, qiymat in lugat.items():
#         if isinstance(qiymat, (int, float)):
#             lugat[kalit] = qiymat * 2
#     return lugat

# # Misol lug'at
# lugat = {
#     "A": 10,
#     "B": 5.5,
#     "C": "salom",
#     "D": 20,
#     "E": 3,
#     "F": "dunyo"
# }

# yangilangan_lugat = raqamlarni_ikki_barobar_kopaytir(lugat)
# print("Yangilangan lug'at:", yangilangan_lugat)


#  11 misol 

# def eng_katta_qiymat_kaliti(lugat):
#     eng_katta_kalit = max(lugat, key=lugat.get)
#     return eng_katta_kalit

# lugat = {
#     "A": 10,
#     "B": 5.5,
#     "C": 20,
#     "D": 15,
#     "E": 3
# }

# natija = eng_katta_qiymat_kaliti(lugat)
# print("Eng katta qiymatga ega kalit:", natija)


# 12 misol

# def ortacha_qiymat(lugat):
#     raqamlar = [qiymat for qiymat in lugat.values() if isinstance(qiymat, (int, float))]
#     if raqamlar:
#         return sum(raqamlar) / len(raqamlar)
#     return None

# # Misol
# lugat = {"A": 10, "B": 5.5, "C": 20, "D": 15, "E": 3}
# print("O'rtacha qiymat:", ortacha_qiymat(lugat))  


#  13 misol 

# def birlashtir_va_jamla(lugat1, lugat2):
#     birlashgan = lugat1.copy()
#     for kalit, qiymat in lugat2.items():
#         if kalit in birlashgan:
#             birlashgan[kalit] += qiymat
#         else:
#             birlashgan[kalit] = qiymat
#     return birlashgan

# lugat1 = {"A": 10, "B": 5, "C": 7}
# lugat2 = {"B": 3, "C": 5, "D": 8}
# print("Birlashtirilgan lug'at:", birlashtir_va_jamla(lugat1, lugat2))  


# 14 misol 

# def uzun_va_qisqa_kalit(lugat):
#     eng_uzun = max(lugat, key=len)
#     eng_qisqa = min(lugat, key=len)
#     return eng_uzun, eng_qisqa

# lugat = {"A": 10, "BB": 5, "CCC": 7, "DDDD": 8}
# print("Eng uzun va qisqa kalit:", uzun_va_qisqa_kalit(lugat))  # ('DDDD', 'A')


#  15 misol 

# def stringni_raqamga_aylantir(lugat):
#     for kalit, qiymat in lugat.items():
#         if isinstance(qiymat, str) and qiymat.isdigit():
#             lugat[kalit] = int(qiymat)
#     return lugat

# lugat = {"A": "123", "B": "hello", "C": "456", "D": 789}
# print("Yangilangan lug'at:", stringni_raqamga_aylantir(lugat))  # {'A': 123, 'B': 'hello', 'C': 456, 'D': 789}


#  16 misol 

# def ikki_barobar_qiymat(lugat):
#     yangi_lugat = {kalit: qiymat * 2 if isinstance(qiymat, (int, float)) else qiymat for kalit, qiymat in lugat.items()}
#     return yangi_lugat

# lugat = {"A": 10, "B": 5.5, "C": "hello", "D": 15}
# print("Yangi lug'at:", ikki_barobar_qiymat(lugat))  


#  17 msiol

# def stringni_teskari_aylantir(lugat):
#     yangi_lugat = {kalit: qiymat[::-1] if isinstance(qiymat, str) else qiymat for kalit, qiymat in lugat.items()}
#     return yangi_lugat

# lugat = {"A": "hello", "B": "world", "C": 123, "D": "python"}
# print("Teskari lug'at:", stringni_teskari_aylantir(lugat))  
