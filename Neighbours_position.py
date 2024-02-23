def get__neighbours(i, j, cnt=4):
    di = [1, 1, 0, -1, -1, -1, 0, 1]
    dj = [0, 1, 1, 1, 0, -1, -1, -1]
    return [(i + di[d], j + dj[d]) for d in range(cnt)]


def get_neighbours_from_matrix(tup, matrix):
    try:
        for i in tup:
            row = matrix[i[0]]
            col = row[i[1]]
            print(col, end=" ")
    except:
        raise 'invalid input/range to the matrix'


if __name__ == '__main__':
    lst = [[1, 2, 3, 4, 2],
           [5, 6, 7, 7, 1],
           [4, 8, 9, 9, 2],
           [2, 4, 1, 5, 1]]

    tup = get__neighbours(2, 2, 8)  # 4 neighbours is default, add 8 argument if you want 8 neighbours
    get_neighbours_from_matrix(tup, lst)
