def mymap(func, *iterables):
    return [func(*tup) for tup in zip(*iterables)]


if __name__ == '__main__':
    print(mymap(lambda a, b, c: abs(a) * abs(b) * abs(c), [1, -2, 3, 2],
                                                          [-4, 5, 6, 7],
                                                          [4, -5, -10, 9]))
