def find_pair_values_v2(lst):
    biggest_1 = 0
    bigggest_2 = 0

    for i in range(len(lst)):
        if lst[i] > lst[biggest_1]:
            biggest_1 = i

    for j in range(len(lst)):
        if lst[j] > lst[bigggest_2] and lst[j] != lst[biggest_1]:
            bigggest_2 = j
    return biggest_1, bigggest_2


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    first, second = find_pair_values_v2(lst)
    print(first, second)
