def find_index(arr):
    n = len(arr)
    
    if n < 3:
        return 0 
    
    max_index = arr.index(max(arr))

    for i in range(1, n - 1):
        if arr[0] < arr[i] < arr[n - 1]:
            return i
    
    return 0

arr1 = [3, 8, 2, 5, 1]  
arr2 = [10, 5, 8, 3]       

result1 = find_index(arr1)
result2 = find_index(arr2)

print(f"Massiv {arr1} uchun natija: {result1}")
print(f"Massiv {arr2} uchun natija: {result2}")
