def remove_element_at_index(arr, k):   
    del arr[k]

    return arr

arr = [3, 8, 2, 5, 1]
k = 2  
result = remove_element_at_index(arr, k)

print("O'zgartirilgan massiv:")
print(result)
