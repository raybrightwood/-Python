def two_num_div():
    first_num = float(input("Введите первое число"))
    second_num = float(input("Введите второе число"))

    if second_num == 0:
        div = 0
    else:
        div = first_num / second_num

    return div
print (two_num_div())