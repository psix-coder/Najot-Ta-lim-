a = 7
b = 2
c = 8

def triangle_perimetr(a=a, b=b, c=c):
    return a + b + c

def triangle_area(a=a, b=b, c=c):
    s = triangle_perimetr(a, b, c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5



