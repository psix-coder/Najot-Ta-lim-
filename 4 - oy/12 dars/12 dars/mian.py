import re

user_id = 1

def get_validated_input(prompt, validation_func):
    while True:
        data = input(prompt)
        if validation_func(data):
            return data
        print("Xato kiritildi. Qayta urinib ko'ring.")

def validate_age(age):
    return age.isdigit()

def validate_phone(phone):
    return phone.startswith("+998") and len(phone) == 13 and phone[1:].isdigit()

while True:
    print("Foydalanuvchi ma'lumotlarini kiriting:")

    name = input("Ism: ")
    lastname = input("Familiya: ")
    age = int(get_validated_input("Yosh: ", validate_age))
    phone = get_validated_input("Telefon raqami: ", validate_phone)
    email = input("Email: ")
    address = input("Manzil: ")

    user_data = f"id: {user_id}, Name: {name}, Lastname: {lastname}, Age: {age}, Phone: {phone}, Email: {email}, Address: {address}\n"
    
    with open("users_info.txt", "a") as file:
        file.write(user_data)
    
    print("Ma'lumotlar saqlandi.")
    user_id += 1
    