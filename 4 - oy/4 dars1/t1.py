#  1 Topshiriq

# def counter():
#     count = 0 

#     def increment():
#         nonlocal count
#         count +=1
#         return count
    
#     return increment

# Funksiya = counter()

# print(Funksiya())
# print(Funksiya())
# print(Funksiya())



# 2 Topshiriq

# def son(factor):
#     def son_1(x):
#         return x * factor
#     return son_1

# kopaytirish = son(3)

# natija1 = kopaytirish(5)
# natija2 = kopaytirish(10)
# natija3 = kopaytirish(15)

# print(natija1)
# print(natija2)
# print(natija3)

#  3 Topshiriq

# def adder():
#     total = 0

#     def add(son):
#         nonlocal total
#         total += son
#         return total
    
#     return add 

# yigindi = adder()


# print(yigindi(5))
# print(yigindi(10))
# print(yigindi(3))
# print(yigindi(7))


# 4 Topshiriq

# def adder_subtractor():
#     total = 0 

#     def add(n):
#         nonlocal total  
#         total += n
#         return total

#     def subtract(n):
#         nonlocal total 
#         total -= n
#         return total

#     return add, subtract  


# adder_func, subtractor_func = adder_subtractor()

# print(adder_func(10))
# print(subtractor_func(5))
# print(adder_func(7))
# print(subtractor_func(5))


# 5 topshiriq

# def tan_narx(narx):
#     def chegirma_qosh(chegirma_miqdori):
#         nonlocal narx
#         narx -= chegirma_miqdori
#         return narx
#     return chegirma_qosh

# MahsulotNarxi = tan_narx(200)

# print(MahsulotNarxi(25))
# print(MahsulotNarxi(5))
# print(MahsulotNarxi(15))


# 6 Topshiriq


# def xisob_total():
#     total = 0

#     def xisob():
#         nonlocal total
#         total += 1
#         return total
    
#     return xisob

# Foydalanuvchi_xisobi = xisob_total()

# print(Foydalanuvchi_xisobi())
# print(Foydalanuvchi_xisobi())
# print(Foydalanuvchi_xisobi())

#  7 Toshiriq

# def parol_tekshir(togri_parol):
#     def tekshir_parol(ParolKirit):
#         if ParolKirit == togri_parol:
#             return "Kiritgan parolingiz togri"
#         else:
#             return "Kiritgan parolingiz notogri"
#     return tekshir_parol

# foydalanuvchi_parolini_tekshir = parol_tekshir("abdulloh2007")

# print(foydalanuvchi_parolini_tekshir("abdulloh2007"))
# print(foydalanuvchi_parolini_tekshir("abdulloh007"))
    
#  8 Topshiriq




