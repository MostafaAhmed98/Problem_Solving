def unique_nums(lst):
    unique_out_nums = []
    for i in lst:
        if i in unique_out_nums:
            continue
        else:
            unique_out_nums.append(i)
    return unique_out_nums


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print(unique_nums(lst))
