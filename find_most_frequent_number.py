def find_most_frequent_number(num_lst):
    out_dict = {}
    for i in num_lst:
        if i in out_dict:
            out_dict[i] += 1
        else:
            out_dict[i] = 1
    highest = max(out_dict.values())
    max_keys = [key for key, value in sorted(out_dict.items(), reverse=True) if value == highest]
    return f"The highest frequency is {highest} for values: {max_keys}"


if __name__ == '__main__':
    num_lst = list(map(int, input().split()))
    print(find_most_frequent_number(num_lst))
