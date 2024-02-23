def find_pair_values_v2(lst):
        pos1, pos2 = 0, 1
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[pos1] + lst[pos2] < lst[i] + lst[j]:
                    pos1, pos2 = i, j

        return pos1, pos2


if __name__ == "__main__":
    lst = list(map(int, input().split()))
    print(find_pair_values_v2(lst))
