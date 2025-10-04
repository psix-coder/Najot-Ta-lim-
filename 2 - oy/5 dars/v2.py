def tub_son_tekshirish(n):
    if n <= 1:
        return False  
    if n == 2:
        return True   
    if n % 2 == 0:
        return False  
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True      

son = 54
if tub_son_tekshirish(son):
    print(f"{son} tub son")
else:
    print(f"{son} tub emas")
