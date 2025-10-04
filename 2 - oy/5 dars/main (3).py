# don`t repeat your self

# def
# lambda

def salom(ism, familiya):
    result = f'Assalomu alaykum {ism}, {familiya}'
    return result

# data = salom(ism="Boburjon", familiya="Dadajonov")

# print(data)

def yoshHisobla(yil):
    yosh = 2024-yil
    return yosh

natija_1 = yoshHisobla(2002)
natija_2 = yoshHisobla(2000)
natija_3 = yoshHisobla(2001)


# def chek_is_pair(number):
#     if number %2 == 0:
#         return True
#     else:
#         return False

# def chek_is_pair(number):
#     if number %2 == 0:
#         return True
#     return False

# def chek_is_pair(number):
#     result =  number %2 == 0
#     return result


def chek_is_pair(number:int) -> bool:
    """this fun checs number is pair"""
    return number %2 == 0

# print()
# print(chek_is_pair(9))


for i in range(1,10):
    if chek_is_pair(i):
        print(i)
