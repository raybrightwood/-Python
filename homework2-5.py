# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с
# тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
a = int(input("Введите натуральное число:"))
j = 0

for el in range(len(my_list)):
    if a <= 2:
        my_list.append(a)
    elif a >= my_list[el]:
        my_list.insert(j, a)
    else:
        j = j + 1
        my_list.insert(j + 1, a)
    break
print(my_list)


