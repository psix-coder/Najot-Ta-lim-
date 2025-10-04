# file = open("ismlar.text", "a")
# file.close()


# file = open("ismlar.text", "w")
# file.write("Meni birinchi yozgan faylim! ")
# file.write("\nMeni ikkinchi yozgan faylim! ")

# print(file.read)
# file.close()

import random
import string

# print(random.randint(2,10))
# print(random.choice((1,2,3,4,5,6,7,8,9)))
# print(random.sample(["a","b","f","r","d"],2))


start = int(input("savol nechadan boshlansin? "))
end = int(input("Nechada tugasin! "))

start_number = random.randint(start, end)
end_number = random.randint(start, end)
oper = random.choice(("-","+", "*"))

# way 1 
# question = f"{start_number} {oper} {end_number} = ?"
# print(question)
# if oper == "+":
#     result = start_number + end_number
# elif oper == "-":
#     result = start_number - end_number
# else:
#     result = start_number * end_number

# print(result == int(question))


# print(result == int(question))
# print(eval(f"{start_number} {oper} {end_number} ") == int(question))