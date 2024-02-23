def filter_empty_rows(matrix):
    return print([i for i in matrix if len(i) > 0])


def read_matrix():
    rows = int(input())
    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    return matrix


if __name__ == '__main__':
    lst = read_matrix()
    filter_empty_rows(lst)
