#  1 Topshiriq

# def my_range(start, stop= None, step=1):
#     if stop is None:
#         stop = start
#         start = 0
    
#     if step ==0:
#         return ValueError("Qadamlar nolga tng bolmasligi kerak ")
    
#     current = start
#     if step > 0:
#         while current < stop:
#             yield current
#             current+= step
#     else:
#         while current > stop:
#             yield current
#             current += step

# for i in my_range(3,10,2):
#     print(i)

#  2 Topshiriq

# def word_lengths(text):
#     words = text.split()
#     for word in words:
#         yield len(word) 

# text = "Bu oddiy tekst"
# lengths = word_lengths(text)

# for length in lengths:
#     print(length)

#  3 Topshiriq

# def odd_numbers(limit):
#     number = 1
#     while number <= limit:
#         yield number
#         number += 2  

# for odd in odd_numbers(15):
#     print(odd)

#  4 Topshiriq

# def odd_numbers(limit):
#     number = 0
#     while number <= limit:
#         yield number
#         number += 2  

# for odd in odd_numbers(15):
#     print(odd)

#  5 Topshiriq

# def infinite_sequence():
#     number = 1
#     while True:
#         yield number
#         number += 1

# for num in infinite_sequence():
#     print(num)
#     if num == 10:  
#         break

#  6 Topshiriq

# def square_numbers(limit):
#     for number in range(1, limit + 1):
#         yield number ** 2 

# for square in square_numbers(5):
#     print(square)

#  7 Topshiriq

# def cumulative_sum(sequence):
#     total = 0
#     for number in sequence:
#         total += number  
#         yield total 

# sequence = [1, 2, 3, 4, 5]
# for sum_value in cumulative_sum(sequence):
#     print(sum_value)

# 8 Topshiriq

# def positive_numbers(sequence):
#     for number in sequence:
#         if number > 0:
#             yield number

# sequence = [-3, 0, 4, -1, 5, 9, -2]
# for pos_num in positive_numbers(sequence):
#     print(pos_num)

# 9 Topshiriq

# import random

# def random_numbers(limit):
#     while True:
#         yield random.randint(1, limit)  

# for num in random_numbers(100):
#     print(num)
#     if num > 90:  
#         break


#  10 Topshiriq

# def is_prime(number):
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#         return True
    
# def Prime_numbers():
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1

# for prime in Prime_numbers():
#     print(prime)
#     if prime > 50:
#         break

#  11 Topshiriq

# def text_oqi(text):
#     for i in reversed(text):
#         yield i

# text = "Hello Python!" 
# for i in text_oqi(text):
    # print(i, end="")

# 12 Topshiriq


# def count_numbers(number):
#     count = 1
#     for i in range(1, number+1):
#         count = count * i
#     yield count

# numbers = 5
# for i in count_numbers(numbers):
#     print(i)

#  13 Topshiriq

# def remove_duplicates(input_list):
#     output_list = []
#     for item in input_list:
#         if item not in output_list:  
#             output_list.append(item)  
#     return output_list

# original_list = [1, 2, 3, 1, 2, 4, 5, 3]
# unique_list = remove_duplicates(original_list)

# print(unique_list)

# 14 Topshiriq

# def multiply_by_n(numbers, n):
#     return [number * n for number in numbers]  

# original_list = [1, 2, 3, 4, 5]
# N = 3
# result_list = multiply_by_n(original_list, N)

# print(result_list)

# 15 Topshiriq

# def reserve_list_in(input_list):
#     left = 0
#     right = len(input_list) - 1

#     while left < right:
#         input_list[left], input_list[right] = input_list[left], input_list[right]
#         left += 1
#         right -= 1 


# list_1 = [1,2,3,4,5,6,7,8,9,10]
# reserve_list_in(list_1)

# print(list_1)



#  16 Topshiriq

# def find_min_max(numbers):
#     if not numbers:  
#         return None, None

#     min_value = numbers[0]  
#     max_value = numbers[0]

#     for number in numbers:
#         if number < min_value:
#             min_value = number 
#         if number > max_value:
#             max_value = number
#     return min_value, max_value

# numbers_list = [5, 1, 9, 3, 7, 6, 2]
# min_value, max_value = find_min_max(numbers_list)

# print("Eng kichik qiymat:", min_value)  
# print("Eng katta qiymat:", max_value)   



#  17 topshiriq

# def swap_keys_values(input_dict):
#     swapped_dict = {value: key for key, value in input_dict.items()}
#     return swapped_dict

# original_dict = {'a': 1, 'b': 2, 'c': 3}
# swapped_dict = swap_keys_values(original_dict)

# print("Asl lug'at: ", original_dict)  
# print("Almashtirilgan lug'at: ", swapped_dict)  


#  18 Topshiriq

# def merge_dictionaries(*dicts):
#     merged_dict = {}
#     for d in dicts:
#         merged_dict.update(d) 
#     return merged_dict

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = {'d': 5}

# merged_result = merge_dictionaries(dict1, dict2, dict3)

# print("Birlashtirilgan lugat:", merged_result)


#  19 topshiriq

# def most_frequent_value(input_dict):
#     if not input_dict: 
#         return None

#     value_count = {}
    
#     for value in input_dict.values():
#         if value in value_count:
#             value_count[value] += 1
#         else:
#             value_count[value] = 1
    
#     most_frequent = max(value_count, key=value_count.get)
#     return most_frequent, value_count[most_frequent]  

# sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2, 'f': 2}
# most_frequent, count = most_frequent_value(sample_dict)

# print("Eng ko'p takrorlangan qiymat:", most_frequent)  
# print("Takrorlanish soni:", count )                    
