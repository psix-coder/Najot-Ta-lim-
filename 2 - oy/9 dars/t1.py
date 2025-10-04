from collections import Counter

def has_duplicates(lst):
    counts = Counter(lst)
    return any(count > 1 for count in counts.values())

print(has_duplicates([1, 2, 1, 2]))  # True
print(has_duplicates([1, 2, 1, 2, 1, 2, 3, 3]))  # True
print(has_duplicates([1, 2, 3, 2, 3]))  # False
