def smallest_pair(lst):
    min_value = None
    for pos1, item1 in enumerate(lst):
        for pos2 in range(pos1+1, len(lst)):
            item2 = lst[pos2]
            cur = item1 + item2 + pos2 - pos1
            if min_value is None or min_value > cur:
                min_value = cur
    return min_value


def multiply_numbers(first, second):
    result = 0
    if first < 0:
        first = first * -1
        for i in range(1, first + 1):
            result += second
        result *= -1
    else:
        for i in range(1, first + 1):
            result += second
    return result


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    value = smallest_pair(lst)
    print(value)
