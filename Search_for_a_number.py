# 2 loops
def search_for_num_2_loops_v1(lst, nums_to_be_found):
    for i in range(len(nums_to_be_found)):
        max_index = []
        for j in range(len(lst)):
            if nums_to_be_found[i] == lst[j]:
                max_index.append(j)
        if len(max_index) == 0:
            print(f"Query {nums_to_be_found[i]} answer -1")
            continue
        print(f"Query {nums_to_be_found[i]} answer {max(max_index)}")


def search_for_num_2_loops_v2(lst, nums_to_be_found):
    lst.reverse()
    for i in nums_to_be_found:
        idx = -1
        if i in lst:
            idx = lst.index(i)
            idx = len(lst) - idx - 1
        print('Query', i, 'answer', idx)


def search_for_num_1_loop(lst, nums_to_be_found):
    last_value_pos = [-1] * 501
    for idx, item in enumerate(lst):
        last_value_pos[item] = idx
    for i in nums_to_be_found:
        assert i < len(last_value_pos)
        print(f"Query is {i} answer is {last_value_pos[i]}")


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    nums_to_be_found = list(map(int, input().split()))
    # search_for_num_2_loops_v1(lst, nums_to_be_found)
    # search_for_num_2_loops_v2(lst, nums_to_be_found)
    search_for_num_1_loop(lst, nums_to_be_found)
