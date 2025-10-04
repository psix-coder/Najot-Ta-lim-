
user_input = input("Matnni kiriting: ")

updated_text = ""

index = 0

while index < len(user_input):
    char = user_input[index]  
    if char == 'e':  
        updated_text += '3' 
    else:
        updated_text += char  
    index += 1  

print("Yangilangan matn:", updated_text)


