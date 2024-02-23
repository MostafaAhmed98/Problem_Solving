
def find_pair_values(lst):
    max_values = []
    max_value = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] != lst[j]:
                value = lst[i] + lst[j]
                if value > max_value:
                    max_value = value
        max_values.append(max_value)
        max_value = 0
    return print(max(max_values))


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    find_pair_values(lst)
