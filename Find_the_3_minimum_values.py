def find_min_3_values(lst):
    min_values = []
    for item in lst:
        min_values.append(item)
        if len(min_values) > 3:
            min_values.sort()
            min_values.pop()
    min_values.sort()
    return min_values


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print(find_min_3_values(lst))
