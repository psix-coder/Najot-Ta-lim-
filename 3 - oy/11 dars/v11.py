# # 1 topshiriq

# class Kitob:
#     def __init__(self, nomi, muallif, nashr_yili):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.nashr_yili = nashr_yili
    
#     def malumot(self):
#         return f"{self.nomi} kitobi {self.muallif} tomonidan {self.nashr_yili} yilda nashr etilgan."

# kitob1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 1926)
# kitob2 = Kitob("Yulduzli tunlar", "Pirimqul Qodirov", 1978)

# print(kitob1.malumot())
# print(kitob2.malumot())


#  2 topshiriq

import openpyxl

try:
    work_book = openpyxl.Workbook()
    work_set = work_book.active
    work_set.title = "User Data"

    user_values = {
        "Foydalanuvchi_1": {"Name": "Able", "Age": 30, "Email": "Able@example.com"},
        "Foydalanuvchi_2": {"Name": "Bob", "Age": 25, "Email": "bob@example.com"},
        "Foydalanuvchi_3": {"Name": "Charlie", "Age": 35, "Email": "charlie@example.com"}
    }

    sarlavha = list(user_values["Foydalanuvchi_1"].keys())
    work_set.append(["User"] + sarlavha)

    for user, attributes in user_values.items():
        row = [user] + [attributes.get(key, "") for key in sarlavha]
        work_set.append(row)

    work_book.save("XL.xlsx")
    print("Fayl muvaffaqiyatli saqlandi: XL.xlsx")

except Exception as e:
    print(f"Xatolik yuz berdi: {e}")


class User:
    def __init__(self, user, name, nom):
        self.user = user 
        self.name = name
        self.nom

