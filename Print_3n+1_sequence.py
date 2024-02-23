def print_3n_1_sequence(n):
    print(n, end=' ')
    if n == 1:
        return
    if n % 2 == 0:
        print_3n_1_sequence(n // 2)
    else:
        print_3n_1_sequence(3 * n + 1)


if __name__ == '__main__':
    print_3n_1_sequence(9)
