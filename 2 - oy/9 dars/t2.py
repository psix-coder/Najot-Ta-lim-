from collections import Counter

def has_all_unique_elements(lst):
    counts = Counter(lst)
    return all(count == 1 for count in counts.values())

print(has_all_unique_elements([1, 2, 1, 2]))  
print(has_all_unique_elements([1, 2, 3, 4]))  
print(has_all_unique_elements([1, 2, 1, 2, 1, 2, 3, 3]))  
print(has_all_unique_elements([1, 2, 3, 4, 5]))  
