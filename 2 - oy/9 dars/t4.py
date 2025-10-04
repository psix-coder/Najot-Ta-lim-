def find_largest_difference(lst):
    if not lst:
        raise ValueError("Ro'yxat bo'sh bo'lishi mumkin emas")

    largest = max(lst)
    smallest = min(lst)
    
    difference = largest - smallest
    
    return difference

print(find_largest_difference([3, 1, 4, 1, 5, 9, 2]))  
print(find_largest_difference([10, 20, 30, 40, 50]))   
print(find_largest_difference([5]))                      
print(find_largest_difference([-10, 0, 10]))             
