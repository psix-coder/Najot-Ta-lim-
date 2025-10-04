def is_prime(num):
   
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                tokens = line.split()
                for token in tokens:
                    try:
                        number = int(token)
                        if is_prime(number):
                            primes.append(number)
                    except ValueError:
                        continue
    except FileNotFoundError:
        print(f"Fayl '{file_path}' topilmadi.")
        return None
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return None
    
    return primes

file_path = input("Faylning to'liq yo'lini kiriting: ")

primes = find_primes_in_file(file_path)

if primes is not None:
    print("Fayldagi tub raqamlar:")
    print(primes)
