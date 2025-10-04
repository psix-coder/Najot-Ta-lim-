
from collections import defaultdict
import re

def count_words_in_file(file_path):
    word_count = defaultdict(int)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                words = re.findall(r'\b\w+\b', line.lower())
                for word in words:
                    word_count[word] += 1
    except FileNotFoundError:
        print(f"Fayl '{file_path}' topilmadi.")
        return None
    except Exception as e:
        print(f"Xato yuz berdi: {e}")
        return None
    
    return dict(word_count)

def print_word_counts(word_counts):
    if word_counts:
        print("So'zlar va ularning sonlari:")
        for word, count in word_counts.items():
            print(f"{word}: {count}")

file_path = input("Faylning to'liq yo'lini kiriting: ")

word_counts = count_words_in_file(file_path)

print_word_counts(word_counts)
