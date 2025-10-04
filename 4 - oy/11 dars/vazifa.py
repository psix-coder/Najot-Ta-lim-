# import asyncio

# # 1. Paroldagi raqamlarni olib tashlash
# async def remove_numbers_from_password(password):
#     new_password = ""
#     index = 0
#     while index < len(password):
#         if not password[index].isdigit():
#             new_password += password[index]
#         index += 1
#     return new_password

# # 2. Matnning faqat birinchi 10 belgisini chiqarish
# async def first_ten_characters(text):
#     new_text = ""
#     index = 0
#     while index < len(text) and index < 10:
#         new_text += text[index]
#         index += 1
#     return new_text

# # 3. Ismdagi raqamlarni olib tashlash
# async def remove_numbers_from_name(name):
#     new_name = ""
#     index = 0
#     while index < len(name):
#         if not name[index].isdigit():
#             new_name += name[index]
#         index += 1
#     return new_name

# # 4. Katta harflarni kichik harflarga o'zgartirish va bo'sh joylarni olib tashlash
# async def lowercase_and_trim_spaces(text):
#     new_text = ""
#     index = 0
#     while index < len(text):
#         char = text[index].lower()
#         if char != ' ':
#             new_text += char
#         index += 1
#     return new_text

# # 5. Unli harflarni chiqarish
# async def extract_vowels(text):
#     vowels = "aeiou"
#     new_text = ""
#     index = 0
#     while index < len(text):
#         if text[index].lower() in vowels:
#             new_text += text[index]
#         index += 1
#     return new_text

# # 6. "a" va "b" ketma-ket kelayotgan bo'lsa, uni "#" belgisiga o'zgartirish
# async def replace_ab_with_hash(word):
#     new_word = ""
#     index = 0
#     while index < len(word):
#         if index < len(word) - 1 and word[index] == 'a' and word[index + 1] == 'b':
#             new_word += '#'
#             index += 2  # "ab" belgilari o'rnini bosadi
#         else:
#             new_word += word[index]
#             index += 1
#     return new_word

# # 7. Raqamli matnni orqaga teskari qilish
# async def reverse_if_all_digits(text):
#     if all(char.isdigit() for char in text):
#         return text[::-1]
#     return text

# # 8. So'zning o'rtasidagi harfni olib tashlash
# async def remove_middle_character(word):
#     index = len(word) // 2  # O'rtadagi indeks
#     return word[:index] + word[index + 1:]

# # 9. "a" harfi bilan tugasa, kichik harflarga o'zgartirish
# async def lowercase_if_ends_with_a(name):
#     if name.endswith('a'):
#         return name.lower()
#     return name

# 10. Takrorlanayotgan harflarni olib tashlash
# async def remove_repeated_characters(text):
#     new_text = ""
#     seen = set()
#     index = 0
#     while index < len(text):
#         if text[index] not in seen:
#             new_text += text[index]
#             seen.add(text[index])
#         index += 1
#     return new_text

# 11 misol
# async def uppercase_if_all_vowels(word):
#     if all(char in "aeiouAEIOU" for char in word):
#         return word.upper()
#     return word

# async def main():
#     print("1. Raqamlar olib tashlangan parol:", await remove_numbers_from_password("Pa55w0rd123!"))
#     print("2. Birinchi 10 belgi:", await first_ten_characters("Hello, world!"))
#     print("3. Raqamlar olib tashlangan ism:", await remove_numbers_from_name("John123"))
#     print("4. Kichik harflarga o'zgartirilgan matn:", await lowercase_and_trim_spaces("   HeLLo WoRLd   "))
#     print("5. Unli harflar:", await extract_vowels("Hello, world!"))
#     print("6. 'ab' ketma-ketligi:", await replace_ab_with_hash("cabare"))
#     print("7. Raqamli matn teskari:", await reverse_if_all_digits("12345"))
#     print("8. O'rtadagi harf olib tashlangan so'z:", await remove_middle_character("example"))
#     print("9. Kichik harfga o'zgartirilgan ism:", await lowercase_if_ends_with_a("Anna"))
#     print("10. Takrorlanayotgan harflar:", await remove_repeated_characters("banana"))
#     print("11. Faqat unli harflar bo'lsa:", await uppercase_if_all_vowels("aeiou"))

# asyncio.run(main())
