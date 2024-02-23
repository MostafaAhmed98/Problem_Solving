def search_for_a_number_v1(num_lst, query_lst):
    def get_key_by_value(dct, value):
        for key, val in dct.items():
            if val == value:
                return key
        return None

    out_dict = {}
    for index, item in enumerate(num_lst):
        out_dict[index] = item
    out_dict = dict(sorted(out_dict.items(), reverse=True))
    for i in query_lst:
        if i in out_dict.values():
            print(f"Query {i} answer {get_key_by_value(out_dict, i)}")
        else:
            print(f"Query {i} answer -1")


def search_for_a_number_v2(num_lst, query_lst):
    out_dict = {}
    for idx, value in enumerate(num_lst):
        out_dict[value] = idx
    for q in query_lst:
        ans = out_dict.get(q, -1)
        print(f"Query {q} answer {ans}")


if __name__ == '__main__':
    num_lst = list(map(int, input().split()))
    num_query = list(map(int, input().split()))
    search_for_a_number_v1(num_lst, num_query)
    print()
    search_for_a_number_v2(num_lst, num_query)
