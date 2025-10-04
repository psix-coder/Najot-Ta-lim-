

def j_avto_validation(raqam:str) -> bool:
    return (
        len(raqam) == 8 
        and raqam[:2].isdigit() 
        and raqam[2].isupper() 
        and raqam[3:6].isdigit() 
        and raqam[6:].isupper()
        )

def y_avto_validation(raqam:str) -> bool:
    return (
        len(raqam) == 8 
        and raqam[:2].isdigit() 
        and raqam[5:7].isupper() 
        and raqam[2:5].isdigit() 
        )



parkovka = {}
a = True

while a:
    son = input('Avto raqam kiriting yoki stop deb yozing ')
    if  son.lower() != 'stop' and j_avto_validation( son):
        if son not in parkovka:
            parkovka[son] = 1
        else:
            parkovka[son] += 1
    
    elif son.lower() != 'stop' and y_avto_validation(son):
        if son not in parkovka:
            parkovka[son] = 1
        else:
            parkovka[son] += 1

    else:
        
        print('Smen yopildi')
        print(f"kirishlar soni {sum(parkovka.values())}")
        print(f"avtolar soni {len(parkovka)}")
        a = False

summa = sum(parkovka.values()) * 4000
print(f"jami ye`gilgan summa{summa}")