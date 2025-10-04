# 1 Topshiriq

# def harf_sana(text):
#     faqat_harf = [char for char in text if char.isalpha()]
#     return len(faqat_harf)

# matn = "Hello Python"
# result = harf_sana(matn)
# print(f"Matnda {result} ta harf bor")


# 2 Topshiriq

# def multiply_by_three(numbers):
#     return [num * 3 for num in numbers]

# numbers = [1, 2, 3, 4, 5]
# result = multiply_by_three(numbers)
# print(result)


# 3 Topshiriq

# def add_lists(list1, list2):
#     return [x + y for x, y in zip(list1, list2)]

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = add_lists(list1, list2)
# print(result)


# 4 Topshiriq

# def get_last_letters(words):
#     return [word[-1] for word in words if word] 

# words = ["apple", "banana", "cherry"]
# result = get_last_letters(words)
# print(result)  


# 5 Topshiriq

# def divide_greater_than_five(numbers):
#     return [num / 10 for num in numbers if num > 5]

# numbers = [3, 7, 10, 4, 15]
# result = divide_greater_than_five(numbers)
# print(result) 


# 6 Topshiriq

# def capitalize_strings(strings):
#     return [s.upper() for s in strings]

# variables = ["name", "age", "country"]
# result = capitalize_strings(variables)
# print(result)  



# 7 Topshiriq

# def add_squares(list1, list2):
#     return [x**2 + y**2 for x, y in zip(list1, list2)]

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# result = add_squares(list1, list2)
# print(result)  



# 8 Topshiriq

# def remove_empty_strings(strings):
#     return [s for s in strings if s]

# strings = ["apple", "", "banana", " ", "cherry"]
# result = remove_empty_strings(strings)
# print(result)  


# 9 Topshiriq

# def extract_number_strings(strings):
#     return [s for s in strings if s.isdigit()]

# strings = ["123", "apple", "456", "banana", "789"]
# result = extract_number_strings(strings)
# print(result)  


# 10 Topshiriq

# def filter_greater_than_100(numbers):
#     return [num for num in numbers if num > 100]

# numbers = [50, 150, 200, 75, 120]
# result = filter_greater_than_100(numbers)
# print(result) 


# 11 Topshiriq


# def filter_palindromes(words):
#     return [word for word in words if word == word[::-1]]

# words = ["level", "apple", "radar", "banana", "civic"]
# result = filter_palindromes(words)
# print(result)  


# 12 Topshiriq

# def filter_uppercase_names(names):
#     return [name for name in names if name.isupper()]

# names = ["ALICE", "Bob", "CHARLIE", "dave"]
# result = filter_uppercase_names(names)
# print(result)  


# 13 Topshiriq

# def filter_three_letter_words(words):
#     return [word for word in words if len(word) == 3]

# words = ["cat", "dog", "apple", "bat", "sun"]
# result = filter_three_letter_words(words)
# print(result)  

# 14 Topshiriq

# def filter_positive_numbers(numbers):
#     return [num for num in numbers if num > 0]


# numbers = [-5, 10, -3, 8, -1]
# result = filter_positive_numbers(numbers)
# print(result) 


def son(numbers):
    return[num for num in numbers if num > 0 ]


nuumbers = [-1, 2, -3, 4, -5, 6 ,-7, 8, -9]
result = son(nuumbers)
print(results)