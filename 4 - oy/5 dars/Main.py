# 1 topshiriq

# raqamlar = [ 1,2,3,4,5,6,7,8,9,10]

# juft = []
# toq = []

# for raqam in raqamlar:
#     if raqam % 2  == 0:
#         juft.append(raqam)
#     else:
#         toq.append(raqam)


# print("Juft raqamlar: ", juft)
# print("Toq sonlar:", toq)

#  2 Topshiriq

# raqam = [ 1,2,3,4,5,6,7,8,9,10]

# yigndi = 0
# indeks = 0 

# while indeks < len(raqam):
#     yigndi += raqam[indeks]
#     indeks += 1


# print("Raqamlar yigindisi:", yigndi)

# 3 Topsjiriq

# def aylanti(royxat):
#     if len(royxat) == 0:
#         return royxat
#     element_1 = royxat.pop(0)
#     royxat.append(element_1)
#     return royxat

# son = [1,2,3,4]
# result = aylanti(son)
# print(result)

#  4 topshiriq

# def raqam_top(royxat):
#     if len(royxat) == 0:
#         return None, None
    
#     eng_kichik = min(royxat)
#     eng_katta = max(royxat)
    
#     return eng_kichik, eng_katta 

# son = [3, 6, 5, 9, 8, 1, 2, 4, 8, 7]
# eng_kichik, eng_katta = raqam_top(son)

# print("Eng katta son:", eng_katta)
# print("Eng kichik son:", eng_kichik)

# 5 Topshiriq

# def qiymat_tekshir(royxat, qiymat):
#     for element in royxat:
#         if element == qiymat:
#             return True  
#     return False  

# raqamlar = [3, 6, 5, 9, 8, 1, 2, 4, 8, 7]
# kiritilgan_qiymat = 5

# bor_yoki_yok = qiymat_tekshir(raqamlar, kiritilgan_qiymat)

# if bor_yoki_yok:
#     print(f"{kiritilgan_qiymat} ro'yxatda bor.")
# else:
#     print(f"{kiritilgan_qiymat} ro'yxatda yo'q.")


#  6 Topshiriq

# def unikal_elementlar(royxat):
#     unikal = []  
#     for element in royxat:
#         if element not in unikal: 
#             unikal.append(element)  
#     return unikal

# raqamlar = [3, 6, 5, 9, 8, 1, 2, 4, 8, 7, 5, 6, 9]
# natija = unikal_elementlar(raqamlar)

# print("Unikal elementlar:", natija)


#  7 Topshiriq

# def teskari_sozlar(royxat):
#     teskari_royxat = []  
#     for soz in royxat:
#         teskari_royxat.append(soz[::-1])  
#     return teskari_royxat


# sozlar = ["salom", "dunyo", "python", "programming", "Abdulloh"]
# natija = teskari_sozlar(sozlar)

# print("Teskari so'zlar:", natija)


# 8 Topshiriq

# def eng_uzun_soz(royxat):
#     if len(royxat) == 0:
#         return None 
    
#     eng_uzun = royxat[0]  
#     for soz in royxat:
#         if len(soz) > len(eng_uzun):  
#             eng_uzun = soz  

#     return eng_uzun

# sozlar = ["salom", "dunyo", "python", "programming", "AI", "mehanizashtirilmagandandurda"]
# natija = eng_uzun_soz(sozlar)

# print("Eng uzun so'z:", natija)


# 9 Topshiriq

# def katta_harflar(royxat):
#     katta_royxat = [] 
#     for soz in royxat:
#         katta_royxat.append(soz.upper())
#     return katta_royxat

# sozlar = ["salom", "dunyo", "python", "programming"]
# natija = katta_harflar(sozlar)

# print("Katta harflar:", natija)

# 10 topshiriq

# def bosh_harfi_katta(royxat):
#     katta_harflar = []  
#     for soz in royxat:
#         if soz[0].isupper():  
#             katta_harflar.append(soz) 
#     return katta_harflar

# sozlar = ["salom", "Dunyo", "python", "Programmer", "kitob", "Odam"]
# natija = bosh_harfi_katta(sozlar)

# print("Bosh harfi katta so'zlar:", natija)

#  11 Topshiriq

# def sozlar_uzunligi(royxat):
#     uzunliklar = []  
#     for soz in royxat:
#         uzunliklar.append(len(soz))  
#     return uzunliklar

# sozlar = ["salom", "dunyo", "python", "programming"]
# natija = sozlar_uzunligi(sozlar)

# print("So'zlarning uzunliklari:", natija)


# 12 Topshiriq

# def qidir_soz(royxat, kiritilgan_soz):
#     if kiritilgan_soz in royxat:  
#         return f"{kiritilgan_soz} ro'yxatda bor."
#     else:
#         return f"{kiritilgan_soz} ro'yxatda yo'q."

# sozlar = ["salom", "dunyo", "python", "programming"]
# kiritilgan_soz = input("Qidirilayotgan so'zni kiriting: ") 
# natija = qidir_soz(sozlar, kiritilgan_soz)
# print(natija)


# 13 Topshiriq

# def kichik_harflar(royxat):
#     kichik_royxat = []  
#     for soz in royxat:
#         kichik_royxat.append(soz.lower())  
#     return kichik_royxat

# sozlar = ["SalOm", "DUNYO", "PyThon", "ProgRamMing"]
# natija = kichik_harflar(sozlar)

# print("Kichik harflar:", natija)

#  14 Topshiriq

# def sozni_ochir(royxat, kiritilgan_soz):
#     if kiritilgan_soz in royxat: 
#         royxat.remove(kiritilgan_soz)  
#         return f"{kiritilgan_soz} ro'yxatdan o'chirildi."
#     else:
#         return f"{kiritilgan_soz} ro'yxatda yo'q."

# sozlar = ["salom", "dunyo", "python", "programming"]
# kiritilgan_soz = input("O'chiriladigan so'zni kiriting: ")  

# natija = sozni_ochir(sozlar, kiritilgan_soz)
# print(natija)
# print("Yangilangan ro'yxat:", sozlar)

#  15 Topshiriq

# def qidir_soz_index(royxat, kiritilgan_soz):
#     try:
#         index = royxat.index(kiritilgan_soz)  
#         return f"{kiritilgan_soz} ro'yxatda {index}-indeksda joylashgan."
#     except ValueError:
#         return f"{kiritilgan_soz} ro'yxatda yo'q."

# sozlar = ["salom", "dunyo", "python", "programming"]
# kiritilgan_soz = input("Qidirilayotgan so'zni kiriting: ")  

# natija = qidir_soz_index(sozlar, kiritilgan_soz)
# print(natija)


# Siqilib kettim to'grisi!