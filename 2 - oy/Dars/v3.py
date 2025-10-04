words = {"apple", "banana", "cherry", "date"}  

all_letters = set()  

for word in words:  
    for letter in word:  
        all_letters.add(letter)  

print(f"Umumiy harflar soni: {len(all_letters)}") 
