def unique_nums(lst):
    unique_out_nums = []
    for idx, item in enumerate(lst):
        if idx == 0 or lst[idx] != lst[idx - 1]:
            unique_out_nums.append(item)
    return unique_out_nums


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print(unique_nums(lst))
