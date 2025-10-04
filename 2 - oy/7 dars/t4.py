def davlatlar_tel_raqami(p_numbers):

    uz_phone_number = []
    us_phone_number = []
    ru_phone_number = []

    for number in p_numbers:
        if number.startswith("+998"):
            uz_phone_number.append(number)  
        elif number.startswith("+7"):
            ru_phone_number.append(number)  
        elif number.startswith("+1"):
            us_phone_number.append(number)  
        else:

            print(f"Nomalum mamlakat telefon raqamini kiriting: {number}")

    return{
        "O'zbekiston": uz_phone_number,
        "Rossiya": ru_phone_number,
        "Amerika": us_phone_number
    }
p_numbers = ["+998911303064", "+794548774459", "+14385001031"] 
result = davlatlar_tel_raqami(p_numbers)

for mamlakat, raqami in result.items():
    print(f"{mamlakat} telefon raqami: ")
    for number in raqami:
        print(number)
        print()