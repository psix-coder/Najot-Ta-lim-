
def is_prime(son):
    if son < 2:
        return False
    for i in range(2, int(son ** 0.5) + 1):
        if son % i == 0:
            return False
    return True

def find_odd_numbers(fayl):
    with open(f"{fayl}", "r") as fayl:
        content = fayl.read()
    words = content.split()
    son = []
    for word in words:
        if word.isdigit():
            son.append(int(word))
    prime_numbers = []
    for number in son:
        if is_prime(son):
            prime_numbers.append(number)
    return prime_numbers

def count_unli_sozlarda(fayl):
    with open(f'{fayl}', 'r') as fayl:
        content = fayl.read()
    soz = content.split()
    unlilar_soni = 0
    for char in content:
        if char in unlilar:
            unlilar_soni += 1
    
    return unlilar_soni


unlilar = "aeiouAEIOU"
def count_unlilar(soz):
    count_unlilar = 0
    
    for unli in soz:
        if unli in unlilar:
            count_unlilar += 1
    return count_unlilar

def find_extreme_vowel_consonant_words(fayl):
    with open(f"{fayl}", "r") as fayl:
        content = fayl.read()
    soz = content.split()
    undosh = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    max_unli = max(soz, key=count_unlilar)
    max_undosh = max(soz, key=lambda word: sum(1 for char in word if char in undosh))

    return max_unli, max_undosh


def count_words(fayl):
    with open(f"{fayl}", "r") as fayl:
        content = fayl.read()
    words = content.split()
    return len(words)
