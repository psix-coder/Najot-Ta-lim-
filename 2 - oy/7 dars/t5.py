def generate_odd_numbers(n):
    odd_numbers = []
    
    current_number = 1
    while len(odd_numbers) < n:
        if current_number % 2 != 0:
            odd_numbers.append(current_number)
        current_number += 1
    
    return odd_numbers

n = 5  
result = generate_odd_numbers(n)

print(f"{n} ta toq sondan tashkil topgan ro'yxat:")
print(result)