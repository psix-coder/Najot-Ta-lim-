import re
from collections import defaultdict

def unli_undosh(word):
    """So'zdagi unli va undosh harflarni sanaydigan funksiya."""
    vowels = 'aeiou'
    num_vowels = sum(1 for char in word if char in vowels)
    num_consonants = sum(1 for char in word if char.isalpha() and char not in vowels)
    return num_vowels, num_consonants

def unli_undosh(file_path):
    max_vowels = 0
    max_consonants = 0
    word_with_max_vowels = None
    word_with_max_consonants = None

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    num_vowels, num_consonants = unli_undosh(word)

                    if num_vowels > max_vowels:
                        max_vowels = num_vowels
                        word_with_max_vowels = word

                    if num_consonants > max_consonants:
                        max_consonants = num_consonants
                        word_with_max_consonants = word
    except FileNotFoundError:
        print(f"Fayl '{file_path}' topilmadi.")
        return None, None
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return None, None
    
    return word_with_max_vowels, word_with_max_consonants

def print_results(word_with_max_vowels, word_with_max_consonants):
    if word_with_max_vowels is not None:
        print(f"Eng ko'p unli harflarga ega so'z: '{word_with_max_vowels}'")
    else:
        print("Unli harflarga ega so'z topilmadi.")
    
    if word_with_max_consonants is not None:
        print(f"Eng ko'p undosh harflarga ega so'z: '{word_with_max_consonants}'")
    else:
        print("Undosh harflarga ega so'z topilmadi.")

file_path = input("Faylning to'liq yo'lini kiriting: ")

word_with_max_vowels, word_with_max_consonants = unli_undosh(file_path)

print_results(word_with_max_vowels, word_with_max_consonants)
re