def max_value(matrix):
    max_value = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > max_value[0]:
                max_value[0] = matrix[i][j]
                max_value[1] = (i, j)
    return print(f"Max value at position {max_value[1]} with value = {max_value[0]}")


def max_value_pyth(matrix):
    max_value = max((matrix[i][j], (i, j)) for i in range(len(matrix)) for j in range(len(matrix[0])))
    return print(f"Max value at position {max_value[1]} with value = {max_value[0]}")


def read_matrix():
    rows = int(input())
    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    return matrix


if __name__ == '__main__':
    matrix = [
        [47, 15, 82, 91],
        [63, 24, 13, 57],
        [89, 88, 12, 30],
        [74, 16, 55, 66],
        [25, 39, 46, 20],
        [96, 53, 42, 45],
        [82, 12, 71, 91],
        [34, 86, 52, 49],
        [61, 92, 38, 67],
        [23, 71, 10, 83],
        [43, 72, 31, 64],
        [54, 38, 77, 18],
        [78, 48, 92, 69],
        [81, 59, 16, 32],
        [62, 89, 58, 13],
        [95, 17, 70, 28],
        [53, 68, 76, 25],
        [30, 59, 27, 75],
        [42, 47, 81, 63],
        [44, 80, 26, 40]
    ]

    max_value(matrix)
