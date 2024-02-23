def my_reduce_sum(func, iterable):
    if len(iterable) == 0:
        return 0

    result = iterable[0]
    for i in range(1, len(iterable)):
        result = func(result, iterable[i])
    return result


def my_reduce_max(func, iterable, init=None):
    if not iterable:
        if init is not None:
            raise TypeError('reduce of empty sequence with no initial value')
        return init
    for item in iterable:
        if init is None:
            init = item
        else:
            init = func(init, item)
    return init


if __name__ == '__main__':
    res_sum = my_reduce_sum(lambda x, y: x + y, [2, 5, 6, 7, 8, 9, 2, 3, 2, 10, 19, 23])
    print(res_sum, sum([2, 5, 6, 7, 8, 9, 3, 2, 2, 10, 19, 23]))
    res_max = my_reduce_max(lambda x, y: x if x > y else y, [2, 5, 6, 7, 8, 9, 3, 2, 10, 19, 23])
    print(res_max, max([2, 5, 6, 7, 8, 9, 3, 2, 10, 19, 23]))
