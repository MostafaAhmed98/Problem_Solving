def swap_two_columns(pos1, pos2, matrix):
    lst = [list(i) for i in zip(*matrix)]
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return [i for i in zip(*lst)]


def read_matrix():
    rows = int(input())
    matrix = [0] * rows
    for i in range(rows):
        matrix[i] = list(map(int, input().split()))
    return matrix


if __name__ == '__main__':
    matrix = read_matrix()
    pos1, pos2 = map(int, input().split())
    swapped_matrix = swap_two_columns(pos1, pos2, matrix)
    print(swapped_matrix)
