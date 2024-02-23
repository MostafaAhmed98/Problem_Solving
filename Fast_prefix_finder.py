def fast_prefix_finder(N, Q):
    out_dict = {}
    for i in range(N):
        input_N = str(input())
        out_dict[i] = input_N
    for i in range(Q):
        input_Q = str(input())
        mathces_value = [value for value in out_dict.values() if input_Q in value]
        if len(mathces_value) == 0:
            print('Not found')
            continue
        print(f"{input_Q} matches {mathces_value}")


if __name__ == '__main__':
    N, Q = 5, 4
    fast_prefix_finder(N, Q)
