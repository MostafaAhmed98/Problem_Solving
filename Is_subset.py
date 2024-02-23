def is_subset(lst, sub_lst):
    unique_sublst = []
    [unique_sublst.append(x) for x in sub_lst if x not in unique_sublst]
    new_lst = [lst[idx:len(unique_sublst)+1] for idx, item in enumerate(lst) if item == unique_sublst[0]]
    return new_lst == [unique_sublst]


if __name__ == '__main__':
    lst1 = [1, 2, 3, 4, 1, 5, 10]
    sub_lst = [2, 3, 4, 1, 3, 1]
    value = is_subset(lst1, sub_lst)
    print(value)
