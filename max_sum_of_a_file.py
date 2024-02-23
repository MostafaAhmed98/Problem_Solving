def max_sum_of_a_file(path):
    with open(path) as file:
        data_pos = [abs(int(i)) for i in file]
    return print(sum(data_pos) * max(data_pos))


if __name__ == '__main__':
    path = 'data.txt'
    max_sum_of_a_file(path)
