
import random

while True:
    starting = input("Dasturni ishga tushraszmi? (ha/yo'q): ")
    correct = 0
    in_correct = 0

    if starting.lower() == "ha":
        ism = input("Ismingizni kiriting: ")
        difficulty = int(input("Qiyinchilik darajasini tanlang (1 dan 5 gacha): "))
        start = 1
        end = 10

        if difficulty == 1:
            start = 1
            end = 10
        elif difficulty == 2:
            start = 10
            end = 20
        elif difficulty == 3:
            start = 20
            end = 50
        elif difficulty == 4:
            start = 50
            end = 100
        elif difficulty == 5:
            start = 100
            end = 1000

        for _ in range(int(input("Necha marotaba savol berilsin?: "))):
            start_number = random.randint(start, end)
            end_number = random.randint(start, end)
            operation = random.choice(["+", "-", "*"])

            question = input(f"{start_number} {operation} {end_number} =? ")
            if eval(f"{start_number} {operation} {end_number}") == int(question):
                print("To'g'ri javob")
                correct += 1
            else:
                print("To'g'ri javob emas")
                in_correct += 1

        with open(f"{ism}_natijalar.txt", 'a') as file:
            file.write(f"\n{ism} - {difficulty} \n Qiyinchilik darajasi {difficulty} \n Barcha to'g'ri javoblar: {correct}\n Noto'g'ri javoblar: {in_correct}")

    elif starting.lower() == "yo'q" or starting.lower() == "yoq":
        print("Dastur to'xtatildi.")
        break

    else:
        print("Xatolik! Iltimos, 'ha' yoki 'yoq' deb javob bering.")

    print(f"\nBarcha to'g'ri javoblar: {correct}, \n Noto'g'ri javoblar: {in_correct}")



with open("my_file.txt", "a") as f:
    f.write("\nBu yangi satr.")


# with open("my_file.txt", "r") as f:
#     content = f.read()
#     print(content)












































