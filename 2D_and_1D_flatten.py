def flatten_to_1d(tup, length):
    row = 0
    if tup[0] < 1:
        row = tup[0]
    elif tup[0] >= 1:
        row = tup[0] * length
    res = row + tup[1]
    return res


def convert_to_2d(num, length):
    row = 0
    while num - length > 0:
        row += 1
        num -= length
    col = num
    return row, col


if __name__ == '__main__':
    lst = [[1, 2, 3, 2],
           [5, 6, 7, 8],
           [4, 8, 9, 5]]
    lst_flatten = [1, 2, 3, 2, 5, 6, 7, 8, 4, 8, 9, 5]
    tup = (0, 2)
    flatten_idx = flatten_to_1d(tup, 4)
    two_d_index = convert_to_2d(flatten_idx, 4)
    print(f"The Flatten index of {tup} is {flatten_idx} and its value in the Flatten list is {lst_flatten[flatten_idx]}")
    print()
    print(f"The 2d index of {flatten_idx} is {two_d_index} and its value in the 2d array is {lst[tup[0]][tup[1]]}")
