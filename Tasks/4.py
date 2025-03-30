
print("Введите номер урока:")
lesson_number = int(input())

if lesson_number < 1 or lesson_number > 10:
    print("Вы ввели некорректное значение. Номер урока должен быть от 1 до 10.")
else:
    lesson_time = 45  
    recess1 = 5      
    recess2 = 15     

    start_hour = 9
    start_minute = 0

    total_minutes = start_hour * 60 + start_minute

    for i in range(1, lesson_number + 1):
        total_minutes += lesson_time


        if i < lesson_number:
            if i % 2 != 0: 
                total_minutes += recess1
            else:          
                total_minutes += recess2

 
    end_hour = total_minutes // 60
    end_minute = total_minutes % 60

    print(f"Урок закончится в {end_hour:02}:{end_minute:02}")