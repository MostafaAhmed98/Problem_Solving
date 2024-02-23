sq = lambda x: x * x


def ff(start, end, step):
    def inner(func):
        sq_nums = [func(vaule) for vaule in range(start, end, step)]
        return sq_nums

    return inner


if __name__ == '__main__':
    processor = ff(2, 6, 1)
    print(processor(sq))
    ff2 = lambda start, end, step: lambda func: [func(value) for value in range(start, end, step)]
    processor_v2 = ff(2, 6, 1)
    print(processor_v2(sq))
