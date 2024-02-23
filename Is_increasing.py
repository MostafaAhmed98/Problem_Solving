def is_increasing(lst):
    ans = ''
    for i in range(1, len(lst)):
        if lst[i] >= lst[i - 1]:
            ans = "YES"
        else:
            ans = "No"
            return ans
    return ans


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    print(is_increasing(lst))
