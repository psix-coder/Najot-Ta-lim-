import openpyxl

work_book = openpyxl.Workbook()
work_set = work_book.active
work_set.title = ("User Data")

num_users = int(input("Necha dona foydalanuvchi bor: "))

user_values = {}

for user_num in range(1, num_users + 1):
    print(f"\n{user_num}-foydalanuvchi ma'lumotlarini kiriting: ")
    user_data = {}
    user_id = input("ID: ")
    user_data["Id: "] = user_id
    user_data["F_name"] = input("Ism: ")
    user_data["L_name"] = input("Familya: ")
    user_data["Age: "] = input("Yosh: ")
    user_values[f"Foydalanuvchi_{user_num}"] = user_data

sarlavha = list(user_values["Foydalanuvchi_1"].keys())
work_set.append(["User"] + sarlavha)

for user, attributes in user_values.items():
    row = [user] + [attributes.get(key, "") for key in sarlavha]
    work_set.append(row)

work_book.save("LL.xlsx")
