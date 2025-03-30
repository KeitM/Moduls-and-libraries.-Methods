import math
print("Введите катет1:")

cathetus1 = int(input())
print("Введите катет2:")
cathetus2 = int(input())


kat = cathetus1**2 + cathetus2**2
gipotenuza = math.sqrt(kat)
print(f"Гипотенуза {math.floor(gipotenuza)}")