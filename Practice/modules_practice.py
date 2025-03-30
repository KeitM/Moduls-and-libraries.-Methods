import random as rand
from datetime import datetime
from datetime import date
import time

print("Это первая часть задания")
print()

print("Привет! Это программа - предсказатель дня. Как тебя зовут?")
name = input()

print(f"Привет,{name}. Загадай число от 1 до 3")

number = int(input())
entered_number = rand.randint(1,3)

if  entered_number  == 1:
     print("О, тебе повезло")
elif  entered_number  == 2:
     print("Удача на твоей стороне")
elif  entered_number  == 3:
     print("Сегодня твой день")
else: 
     print("Попробуй ещё раз ввести число от 1 до 3")

print("Это вторая часть задания")

print("Привет! Сыграем в русскую рулетку? Как тебя зовут?")
name = input()

print(f"Привет,{name}. Загадай число от 1 до 6")

number = int(input())
generated_number = rand.randint(1,6)
#print(generated_number) оставлю просто для проверка рандома

if  number  == generated_number:
     print("Тебе не повезло,ты умер")
elif  number  != generated_number:
     print(f"Ты выжил, пуля была в другом отверстии, это было отверстие № {generated_number}")
else: 
     print("Попробуй ещё раз ввести число от 1 до 6")

print()

print("Это третья часть задания")


today = date.today()

today1 = today.strftime("%B, %d. %Y")

print(f"Привет! Сегодня {today1} года. Введи, пожайлуста, день своего рождения. День вводится без 0, если он меньше 10: 1,2, 3 итд.")

day = int(input())

print(f"Введи, пожайлуста, месяц своего рождения. Месяц вводится без 0, если он меньше 10: 1,2, 3 итд.")

month = int(input())

print(f"Введи, пожайлуста, год своего рождения")

year = int(input())

birthday = datetime(year, month, day)

age = today.year - year - ((today.month, today.day) < (month, day))

rest_days = 0

if year % 100 != 0 and year % 4 == 0:
  rest_days = 366 - ((today.month - month) + (today.day - day))
elif year % 400 == 0:
      rest_days = 366 - ((today.month - month) + (today.day - day))   
else:
        rest_days = 365 - ((today.month - month) + (today.day - day))


print(f"Тебе {age} лет и {rest_days} дней")
