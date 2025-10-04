#  1 Topshiriq

# class MyIterator:
#     def __init__(self):
#         self.current = 1
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current <= 10:
#             num = self.current
#             self.current += 1
#             return num
#         else:
#             raise StopIteration

# my_iter = MyIterator()

# for num in my_iter:
#     print(num)



#  2 Topshiriq

# my_list = [10,20,30,40,50,60,70]

# my_iter = iter(my_list)

# while True:
#     try:
#         element = next(my_iter)
#         print(element)
#     except StopIteration:
#         break



#  3 Topshiriq

# class ReverseIterator:
#     def __init__(self, my_list):
#         self.my_list = my_list        
#         self.index = len(my_list) - 1  
    
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.index >= 0:
#             element = self.my_list[self.index]  
#             self.index -= 1 
#             return element
#         else:
#             raise StopIteration 
        
# my_list = [10, 20, 30, 40, 50]

# reverse_iter = ReverseIterator(my_list)

# for element in reverse_iter:
#     print(element)


#  4 Topshiriq

# my_python = "Hello Python"

# my_iter = iter(my_python)

# while True:
#     try:
#         char = next(my_iter)
#         print(char)
#     except StopIteration:
#         break

#  5 Topshiriq

# my_numbers = [1,2,3,4,5,6,7,8,9,10]

# my_iter = iter(my_numbers)

# while True:
#     try:
#         char = next(my_iter)
#         if char % 2 == 0:
#             print(char)
#     except StopIteration:
#         break


#  6 Topshiriq

# class NumberIterator:
#     def __init__(self, numbers):
#         self.numbers = numbers  
#         self.index = 0          

#     def __iter__(self):
#         return self  
    
#     def __next__(self):
#         if self.index < len(self.numbers):
#             number = self.numbers[self.index]  
#             self.index += 1  
#             return number
#         else:
#             raise StopIteration  

# my_numbers = [1,2,3,4,5,6,7,8,9,10]

# number_iter = NumberIterator(my_numbers)

# total_sum = 0
# for num in number_iter:
#     total_sum += num  
    
# print("Yig'indi:", total_sum)



#  7 Topshiriq


# class ElementIterator:
#     def __init__(self, elements):
#         self.elements = elements  
#         self.index = 0            
    
#     def __iter__(self):
#         return self  
    
#     def __next__(self):
#         if self.index < len(self.elements):
#             element = self.elements[self.index]  
#             self.index += 1  
#             return element
#         else:
#             raise StopIteration  
# def find_element(iterator, target):
#     for element in iterator:
#         if element == target:
#             return True
#     return False

# my_list = [1, 2, 3, 4, 5]

# element_iter = ElementIterator(my_list)

# target_element = 3

# if find_element(element_iter, target_element):
#     print(f"{target_element} ro'yxatda mavjud.")
# else:
#     print(f"{target_element} ro'yxatda mavjud emas.")


#  8 Topshiriq

# password = input("Parolni kiriting: ")

# updated_password = ""

# index = 0

# while index < len(password):
#     char = password[index]  
#     if not char.isdigit():  
#         updated_password += char  
#     index += 1  

# print("Yangilangan parol:", updated_password)


#  9 Topshiriq

# user_input = input("Matnni kiriting: ")

# if len(user_input) > 10:
#     index = 0  
#     output = "" 

#     while index < 10:  
#         output += user_input[index]  
#         index += 1  

#     print("Birinchi 10 belgi:", output)
# else:
#     print("Matn 10 belgidan qisqa yoki teng.")



#  10 Topshiriq

# user_input = input("Matnni kiriting: ")

# output = ""

# index = 0

# while index < len(user_input):
#     char = user_input[index]  
#     if char == 'x':  
#         break  
#     output += char  
#     index += 1  

# print("Natija:", output)



#  11 Topshiriq

# user_input = input("Matnni kiriting: ")

# updated_text = ""

# index = 0

# while index < len(user_input):
#     char = user_input[index]  
#     if char != ' ':  
#         updated_text += char  
#     index += 1  

# print("Yangilangan matn:", updated_text)


#  12 Topshiriq

# user_input = input("Matnni kiriting: ")

# updated_text = ""

# index = 0

# while index < len(user_input):
#     char = user_input[index]  
#     if char == 'e':  
#         updated_text += '3' 
#     else:
#         updated_text += char  
#     index += 1  

# print("Yangilangan matn:", updated_text)


