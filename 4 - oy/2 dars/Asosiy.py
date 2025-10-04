# from Matemathic1 import RaqamlarYigindisi

# 1 Topshiriqniki
# son = 108
# print(RaqamlarYigindisi(son))

# from Mathematics2 import vaqtni_ajrat

# # 2 Topshiriq
# sekundlar_soni = 100000
# natija = vaqtni_ajrat(sekundlar_soni)
# print(natija)

# 3 Topshiriq

from circle import circle_perimeter, circle_area
from triangle import triangle_perimetr, triangle_area
from square import square_perimeter, square_area

print("Aylana Perimaetri:", circle_perimeter())  
print("Aylana Maydini:", circle_area()) 

print("Uchburchak Perimetri:", triangle_perimetr()) 
print("Uchburchak Maydoni:", triangle_area())  

print("Kvadrat Perimetri:", square_perimeter())  
print("Kvadrat maydoni:", square_area())
