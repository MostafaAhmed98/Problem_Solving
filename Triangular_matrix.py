def Triangular_matrix(matrix):
    upper_sum = [sum(matrix[i][i:len(matrix)]) for i in range(len(matrix[0]))]
    lower_sum = [sum(matrix[i][:i + 1]) for i in range(len(matrix[0]))]
    return print(sum(lower_sum), sum(upper_sum))


def read_matrix():
    rows = int(input())
    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    return matrix


if __name__ == '__main__':
    matrix = read_matrix()
    Triangular_matrix(matrix)
