def sort_different_types_v1(lst):
    int_type = sorted([i for i in lst if type(i) is int])
    str_type = sorted([i for i in lst if type(i) is str])
    float_type = sorted([i for i in lst if type(i) is float])
    list_type = sorted([i for i in lst if type(i) is list])
    return int_type + str_type + float_type + list_type


def sort_different_types_v2(lst):
    out_dict = {}
    for item in lst:
        t = type(item)
        out_dict.setdefault(t, [])
        out_dict[t].append(item)
    lsts = [sorted(lst) for lst in out_dict.values()]
    return [item for lst in lsts for item in lst]


if __name__ == '__main__':
    lst = [10, 'most', 2.5, 7, 'aly', 9, 4.5, 2, 'ziad', -4, 1.1, [1, 5], [0, 7, 8]]
    print(sort_different_types_v1(lst))
    print()
    print(sort_different_types_v2(lst))
