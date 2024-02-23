def most_frequent_number(lst):
    number = 10 ^ 6
    repeated = 0
    for i in range(len(lst)):
        counter = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                counter += 1
        if lst[i] < number:
            number = lst[i]
            repeated = counter
    return number, repeated


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    number, repeats = most_frequent_number(lst)
    print(f"{number} repeated {repeats} times")
