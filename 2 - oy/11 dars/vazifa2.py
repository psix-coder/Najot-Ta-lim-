def tel_validation(son:str) -> bool:
    return (
        len(son) == 12
        and son.isdigit()
        and son[:3].startswith(998)
    )

n = str(input("Iltimos telefon raqamingizni kiriting!  "))
print(tel_validation(a))