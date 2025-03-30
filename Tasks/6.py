print("Введите первый момент времени через двоеточие" )

first_time_moment = input().split(":")

hours = int(first_time_moment[0])*3600
munutes = int(first_time_moment[1])*60
seconds = int(first_time_moment[2])

seconds_of_first_time = hours + munutes + seconds

print("Введите 2й момент времени через двоеточие" )

second_time_moment = input().split(":")

hours1 = int(second_time_moment[0])*3600
munutes1 = int(second_time_moment[1])*60
seconds1 = int(second_time_moment[2])

seconds_of_2nd_time = hours1 + munutes1 + seconds1

difference =  seconds_of_2nd_time - seconds_of_first_time

print(f"Разница составила {abs(difference)} секунд")
