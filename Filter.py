def my_filter(func, iterable):
    return [item for item in iterable if func(item)]


if __name__ == '__main__':
    res = my_filter(lambda n: n % 2 == 0, [1, 2, 3, 4, 5, 6, 10, 13, 14])
    print(res)
