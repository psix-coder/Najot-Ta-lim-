i = [
    "Akmal",
    "abror",
    "Abdulloh",
    "Alisher",
    "umidjon",
    "Davronbrk",
    "ali"
    ]

kichik_harflar = []
katta_harflar = []

for harf in i:
    if harf.islower():
        kichik_harflar.append(harf)
    elif harf.istitle():
        katta_harflar.append(harf)

print("Katta harflar:! ", katta_harflar)
print("Kichik harflar:! ", kichik_harflar)