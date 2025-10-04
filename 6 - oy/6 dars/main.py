def salom_ber(ism):
    """
    Foydalanuvchiga salom beruvchi funksiya
    
    Args:
        ism (str): Foydalanuvchi ismi
        
    Returns:
        str: Salom xabari
    """
    return f"Assalomu alaykum, hurmatli {ism}!"

def son_tekshir(son):
    """
    Sonni juft yoki toqligini tekshiruvchi funksiya
    
    Args:
        son (int): Tekshiriladigan son
        
    Returns:
        str: Son haqida ma'lumot
    """
    if son % 2 == 0:
        return f"{son} - juft son"
    else:
        return f"{son} - toq son"

def royxat_yigindi(royxat):
    """
    Ro'yxat elementlari yig'indisini hisoblovchi funksiya
    
    Args:
        royxat (list): Sonlar ro'yxati
        
    Returns:
        int: Ro'yxat elementlari yig'indisi
    """
    return sum(royxat)
