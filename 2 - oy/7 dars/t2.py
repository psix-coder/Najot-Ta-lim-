i = ["A", "a", "B", "b", "C", "c", "D", "d"]

kichik_harflar = []
katta_harflar = []

for harf in i:
    if harf.islower():
        kichik_harflar.append(harf)
    elif harf.isupper():
        katta_harflar.append(harf)

print("Katta harflar:", katta_harflar)
print("Kichik harflar:", kichik_harflar)
