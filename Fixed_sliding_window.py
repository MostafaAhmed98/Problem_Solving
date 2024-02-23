def fixed_sliding_window(lst, k):
    dummy_lst = [0] * 100
    for i in range(len(lst)): # [1, 0, 3, -4, 2, -6, 9]
        if len(lst) - i < k:
            break
        wind_sum = sum(lst[i:k+i])
        dummy_lst[i] = wind_sum
    max_sum = max(dummy_lst)
    return f"Starts at {dummy_lst.index(max_sum)} with Sum {max_sum}"


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    k = int(input())
    value = fixed_sliding_window(lst, k)
    print(value)
