def filter_duplicates_v1(lst):
    out_dict = {}
    for item in lst:
        item = tuple(item)
        out_dict.setdefault(item, 0)
    return [list(item) for item in out_dict.keys()]


def filter_duplicates_v2(lst):
    tpls = [tuple(item) for item in lst]
    out_dict = dict.fromkeys(tpls)
    return [list(i) for i in out_dict]


if __name__ == '__main__':
    lst = [[7, 1], [2, 4], [7, 1], [5, 2], [2, 4]]
    print(filter_duplicates_v1(lst))
    print()
    print(filter_duplicates_v2(lst))
