import math
from datetime import datetime
print("Введите год, пожайлуста" )

year = int(input())

day_of_week = (year + math.floor((year - 1)/4) - math.floor((year - 1)/100) + math.floor((year - 1)/400)) % 7

last_year = 'было'

next_year = 'будет'

if year > int(datetime.now().year):
    match day_of_week:
        case 0:
            print(f"Первого января {year} года {next_year} воскресенье" )
        case 1:
            print(f"Первого января {year} года {next_year} понедельник" )
        case 2:
            print(f"Первого января {year} года {next_year} вторник" )
        case 3:
            print(f"Первого января {year} года {next_year} среда" )
        case 4:
            print(f"Первого января {year} года {next_year} четверг" )
        case 5:
            print(f"Первого января {year} года {next_year} пятница" )
        case 6:
            print(f"Первого января {year} года {next_year} суббота" )
else:
    match day_of_week:
        case 0:
            print(f"Первого января {year} года {last_year} воскресенье" )
        case 1:
            print(f"Первого января {year} года {last_year} понедельник" )
        case 2:
            print(f"Первого января {year} года {last_year} вторник" )
        case 3:
            print(f"Первого января {year} года {last_year} среда" )
        case 4:
            print(f"Первого января {year} года {last_year} четверг" )
        case 5:
            print(f"Первого января {year} года {last_year} пятница" )
        case 6:
            print(f"Первого января {year} года {last_year} суббота" )