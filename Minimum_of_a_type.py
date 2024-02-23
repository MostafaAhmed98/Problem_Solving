def find_smallest(lst, taregt_type):
    new_lst = [item for item in lst if type(item) == taregt_type]
    return min(new_lst)


if __name__ == '__main__':
    lst = [10, -2.5, 20, 5, 'mostafa', 5.2, 'Ziad']
    value = find_smallest(lst, type(5))
    print(value)
