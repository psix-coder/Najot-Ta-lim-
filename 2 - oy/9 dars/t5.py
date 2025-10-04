def count_vowels_and_consonants(s):
    vowels = 'aksjbdfpiqwhflasasoifhwifehaslihfaskjdhf'
    consonants = 'asfhiashfqwklefhjasdifhaskjdfasfuhj'
    
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return vowel_count, consonant_count

word = "Hello, World!"
vowels, consonants = count_vowels_and_consonants(word)
print(f"Unli harflar soni: {vowels}")     
print(f"Undosh harflar soni: {consonants}") 