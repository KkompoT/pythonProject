# Занятия для Самостоятельной работы к 5 уроку

# =================__-1-__=================

num = lambda x: "Четное" if x % 2 == 0 else "Нечетное"
print(num(201))

# =================__-2-__=================
"""Дан список чисел. Вернуть список , где припомощи функции map() каждое число переведено в строку. в качестве
                                    функции в map использовать lambda"""
list1 = [24.51, 24.17, 20.18, 27.57, 25.0, 26.49, 21.0, 24.91, 25.39]
str1 = list(map(lambda x: str(x), list1))
print(type(str1), str1)

# =================__-3-__=================

"""При помощи функции filter из кортежа слов отфлиртовать только те, которые являются полиндромами
(которые читаются одинаково в обе стороны)"""

tuple1 = ("довод", "получил", "ушел", "доход", "заказ")
poly = list(filter(lambda x: x == x[::-1], tuple1))
print(poly)

# =================__-4-__=================

"""Написать декоратор к 2м любым функциям, который бы считал и выводил время их выполнения"""

matrix = [
    [0, 1, 2, 3, 4],
    [10, 11, 44, 12],
    [20, 21, 23, 24],
    [30, 31, 32, 33, 34],
    [40, 41, 42, 43, 44],
]

from datetime import datetime


def decor_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print(f"время выполнения функции: {end - start} секунд.")

    return wrapper


@decor_time
def sum_element():
    s = []
    for string in matrix:
        s.extend(string)
    return sum(s)


@decor_time
def count_element():
    count = 0
    for el in matrix:
        count += len(el)
    return count


sum_element()
count_element()


"""Сделать функцию которая на вход принимает строку. Анализирует ее методом .isdigit
функция умеет распозновать отрицательные числа и десятичные дроби"""
def str1():
    x = input()
    if x.isdigit():
        x = int(x)
        if x > 0:
            print(f"Вы ввели положительное число: {x}")

    else:
        if x[0] == '-' and x[1::].isdigit():
            x = int(x)
            print(f"Вы ввели отрицательное число: {x}")
        else:
            if '.' in x:
                x2 = x.replace('.','')
                if x2[1::].isdigit():
                    x = float(x)
                    if x < 0:
                        print(f"Вы ввели отрицательное дробное число: {x}")
                    else:
                        print(f"Вы ввели положительное дробное число: {x}")
                else:
                    print(f"Вы ввели не кореректное число: {x}")
            else:
                print(f"Вы ввели не кореректное число: {x}")

str1()