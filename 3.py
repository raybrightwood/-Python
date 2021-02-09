def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'результат - {my_func(int(input("введи первое число ")), int(input("введи второе число ")), int(input("введи третье число ")))}')

