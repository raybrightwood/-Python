# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень).
# Напишите решения через list и через dict.

month_dict = {"key_1": 'winter', "key_2": 'spring', "key_3": 'summer', "key_4": 'autumn'}
month_number = int (input("Введите номер месяца"))
if month_number == 12 or month_number ==1 or month_number == 2:
    print(month_dict.get("key_1"))
if month_number == 3 or month_number == 4 or month_number == 5:
    print(month_dict.get("key_2"))
if month_number == 6 or month_number == 7 or month_number == 8:
    print(month_dict.get("key_3"))
if month_number == 9 or month_number == 10 or month_number == 11:
    print(month_dict.get("key_4"))
else:
    print("Введите номер месяца от 1 до 12")
