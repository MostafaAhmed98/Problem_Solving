def reduce_v2_v1(func1_overall, func2_consecutive, iterable):
    if not iterable:
        raise TypeError("The length of the sequence must be at least 2")
    if len(iterable) % 2 != 0:
        raise TypeError("The length of the sequence must be even")
    result = func2_consecutive(iterable[0], iterable[1])
    i = 3
    while True:
        if i > len(iterable):
            break
        result = func1_overall(result, func2_consecutive(iterable[i - 1], iterable[i]))
        i += 2
    return result


def reduce_v2_v2(func1_overall, func2_consecutive, iterable):
    try:
        first, second, *iterable = iterable
        res = func2_consecutive(first, second)
    except:
        return RuntimeError("The length of the sequence must be at least 2")
    while iterable:
        try:
            first, second, *iterable = iterable

        except:
            return RuntimeError("The length of the sequence must be even")
        res = func1_overall(res, func2_consecutive(first, second))
    return res


if __name__ == '__main__':
    print(reduce_v2_v1(lambda x, y: x * y, lambda a, b: a + b, [2, 5, 3, 4, 5, 10]))
    print(reduce_v2_v2(lambda x, y: x * y, lambda a, b: a + b, [2, 5, 3, 4, 5, 10]))
