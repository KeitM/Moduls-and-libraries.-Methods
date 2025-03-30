print("Введите количество пирожков:")
quantity_of_cakes = int(input())
print("Введите стоимость одного пирожка - рубли:")
rubl = int(input())
print("Введите стоимость  одного пирожка - копейки:")
kop = int(input())

rubles = rubl * quantity_of_cakes

if kop < 0 or kop >= 100:
    print("Ошибка: стоимость в копейках должна быть от 0 до 99.")
else:
    total_kopeika = (rubl * 100 + kop) * quantity_of_cakes
 
    total_rubles = total_kopeika // 100
    total_kopecks = total_kopeika % 100
    
print(f"Общая стоимость всех пирожков составит{total_rubles} рублей {total_kopecks} копеек")