# def my_func(x, y):
#     res = x**y
#     return res
#
# print(my_func(float(input("Введит число")), float(input("Введитe степень"))))


def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res


print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))
