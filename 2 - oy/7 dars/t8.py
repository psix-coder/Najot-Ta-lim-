def remove_smallest_from_end(arr):
    if len(arr) == 0:
        return []  

    min_element = min(arr)
    
    arr.remove(min_element)
    
    return arr

arr = [3, 8, 2, 5, 1]
result = remove_smallest_from_end(arr)

print("O'zgartirilgan massiv:")
print(result)
