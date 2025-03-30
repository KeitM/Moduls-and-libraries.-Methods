import math
print("Введите константу а:")

a = int(input())
print("Введите константу b:")
b = int(input())

print("Введите константу c:")
c = int(input())

diskriminant = b*b - 4*a*c

if diskriminant < 0:
   print("Дейстивтельных корней нет")
elif diskriminant == 0:
    kor = - b/ (2*a)
    print(f"Уравнение имеет один корень:{kor}" )
else:
    kor1 = (-b + math.sqrt(diskriminant)) / (2 * a)
    kor2 = (-b - math.sqrt(diskriminant)) / (2 * a)
    print(f"Корни уравнения {kor1} и {kor2}")