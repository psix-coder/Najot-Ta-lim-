n = int(input("n sonni kiriting: "))
kopaytma = 1
bosh = 11
for i in range (1, n + 1):
        kopaytma *= bosh / 10
        bosh += 1
print(kopaytma)