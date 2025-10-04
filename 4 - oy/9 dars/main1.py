import time
import threading

# # 1-misol
# def count(numbers):
#     for num in numbers:
#         count_number = 0
#         for i in str(num):
#             count_number += int(i)
#         print(count_number)


# start = time.time()
# th1 = threading.Thread(target=count, args=([108, 355, 991],))
# th1.start()
# th1.join() 
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")


# # 2-misol
# def time1(time: int):
#     day = int(time) / 86400
#     hour = int(time) / 3600
#     minute = int(time) / 60
#     sekund2 = hour * 3600
#     print(f"{day} Kun; \n{hour} Soat; \n{minute} Minut; \n{sekund2} Sekund")


# start = time.time()
# th1 = threading.Thread(target=time1, args=(int(input("Vaqt kiriting: ")),))
# th1.start()
# th1.join()
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 3-misol
# def upper_string(names: list):
#     new_names= []
#     for i in names:
#         new_names.append(i.title())
#     print(new_names)
# start = time.time()
# th1 = threading.Thread(target=upper_string, args=(['alfred', 'tabitha', 'william', 'arla'],))
# th1.start()
# th1.join()
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 4-misol
# def upper_seventy(numbers: list):
#     upper_numbers = []
#     for i in numbers:
#         if i > 75:
#             upper_numbers.append(i)
#     print(upper_numbers)

# start = time.time()
# th1 = threading.Thread(target=upper_seventy, args=([66, 90, 68, 59, 76, 60, 88, 74, 81, 65],))
# th1.start()
# th1.join()
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 5-misol
# def polidron(names: list):
#     polidron_names = []
#     for i in names:
#         if  i.lower() == i.lower()[::-1]:
#             polidron_names.append(i)
#     print(polidron_names)

# start = time.time()
# th1 = threading.Thread(target=polidron, args=(['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom'],))
# th1.start()
# th1.join()
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 6-misol
# def e_to_three(text):
#     new_text = ""
#     i = 0
#     while i < len(text):
#         if text[i] == "e":
#             new_text += "3"
#         else:
#             new_text += text[i]
#         i += 1
#     print(new_text)

# start = time.time()
# th1 = threading.Thread(target=e_to_three, args=(input("Matn kiriting: "),))
# th1.start()
# th1.join()
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 7-misol
# def i_to_three(text):
#     new_text = ""
#     i = 0
#     while i < len(text):
#         if text[i] == " ":
#             new_text += ""
#         else:
#             new_text += text[i]
#         i += 1
#     print(new_text)
# start = time.time()
# th1 = threading.Thread(target=i_to_three, args=(input("Matn kiriting: "),))
# th1.start()
# th1.join()
# end = time.time()
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 8-misol

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# results = []  

# def multiply(numbers: list):
#     new_list = []
#     for i in numbers:
#         new_list.append(i * 2)
#     results.append(new_list)  
    
# start = time.time()

# th1 = threading.Thread(target=multiply, args=(numbers,))
# th2 = threading.Thread(target=multiply, args=(numbers,))

# th1.start()
# th2.start()

# th1.join()
# th2.join()

# end = time.time()

# print(f"Thread 1 natijasi: {results[0]}")
# print(f"Thread 2 natijasi: {results[1]}")
# print(f"Dastur ishlashi uchun {round(end - start, 2)} sekund vaqti ketdi")

# # 9-misol

# import threading
# import random
# import time

# results = []  

# def generate_random_numbers():
#     random_numbers = [random.randint(1, 100) for _ in range(5)]
#     thread_name = threading.current_thread().name
#     results.append({thread_name: random_numbers})

# start = time.time()

# threads = []
# for i in range(10):
#     thread = threading.Thread(target=generate_random_numbers, name=f"Thread-{i+1}")
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()

# end = time.time()

# for result in results:
#     for thread_name, numbers in result.items():
#         print(f"{thread_name} natijasi: {numbers}")

# print(f"\nDastur ishlashi uchun {round(end - start, 3)} sekund vaqt ketdi")


# print(__name__)