print("Введите трёхзначное число:")
number = int(input())

if number % 1000 < 1:
    print("Введите трёхзначное число:")
else:
   one = number % 10
   dec = number // 10
   dec1 = dec % 10
   hundard = dec // 10
   numbers_sum = one + dec1 + hundard
    
print(f"Сумма цифр {numbers_sum}")