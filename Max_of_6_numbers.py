def my_max2(a, b):
    if a > b:
        return a
    return b


def my_max_3(a, b, c):
    return my_max2(a, my_max2(b, c))


def my_max_4(a, b, c, d):
    return my_max_3(a, my_max_3(b, c, d))


def my_max_5(a, b, c, d, e):
    return my_max_4(a, my_max_4(b, c, d, e))


def my_max_6(a, b, c, d, e, f):
    return my_max_5(a, my_max_5(b, c, d, e, f))


print(my_max_6(1, 2, 3, 4, 5, 6))
