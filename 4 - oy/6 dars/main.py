# users = ["Abdulloh", "Jamoliddin", "Muhmmadjon", "Davron"]

# iter_users = users.__iter__()
# print(iter_users.__next__())
# print(iter_users.__next__())
# print(iter_users.__next__())
# print(iter_users.__next__())



# class CostumItterator:
#     def __init__(self, users, Iterable) -> None:
#         self.users = users
#         self.Iterable = Iterable

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.__index >= len(self.__users):
#             raise StopIteration
#         user = self.__user[self.__index]
#         self.__index +=1
#         return user
    
# users = ["a", "b", "c"]

# iter_users = CostumItterator(users)
# print(iter_users.__next__())
# print(iter_users.__next__())
# print(iter_users.__next__())
# print(iter_users.__next__())


#  1 Topshiriq

# matn = input("Matnni kiriting: ")

# i = 0

# while i < len(matn):
#     print(matn[i].upper(), end="")
#     i += 1


# ism = input("Ismingizni kiriting: ")

# natija = ""

# i = 0

# while i < len(ism):
#     if ism[i].lower() == 'a': 
#         natija += '@'
#     else:
#         natija += ism[i]
#     i += 1

# print(natija)



# parol = input("Parolingizni kiriting: ")

# yangilangan_parol = ""

# i = 0

# while i < len(parol):
#     if not parol[i].isdigit():
#         yangilangan_parol += parol[i]
#     i += 1

# print("Yangilangan parol:", yangilangan_parol)


