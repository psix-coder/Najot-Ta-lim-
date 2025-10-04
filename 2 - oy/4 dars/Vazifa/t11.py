n = int(input("n sonini kiriting: "))
s = 0
for i in range(n, 2*n + 1):
    s += i * i
print(f"Yig'indi : {s}")