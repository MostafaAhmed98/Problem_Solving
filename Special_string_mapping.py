def special_string_mapping_v1(input):
    orig_letters = 'abcdefghijklmnopqrstuvwxyz'
    target_letters = 'YZIMNESTODUAPWXHQFBRJKCGVL'
    orig_nums = '0123456789'
    target_symb = '!@#$%^&*()'
    alpha_dict = {}
    nums_dict = {}
    final_output = ''
    for i, j in zip(orig_letters,target_letters):
        alpha_dict[i] = j
    for i, j in zip(orig_nums,target_symb):
        nums_dict[i] = j
    for i in input:
        if i in alpha_dict.keys():
            final_output += alpha_dict[i]
        elif i in nums_dict.keys():
            final_output += nums_dict[i]
        else:
            final_output += i
    return final_output


def special_string_mapping_v2(input):
    orig_letters = 'abcdefghijklmnopqrstuvwxyz'
    target_letters = 'YZIMNESTODUAPWXHQFBRJKCGVL'
    orig_nums = '0123456789'
    target_symb = '!@#$%^&*()'
    alpha_dict = {orig_letters[i]:target_letters[i] for i in range(len(orig_letters))}
    nums_dict = {orig_nums[i]:target_symb[i] for i in range(len(orig_nums))}
    final_output = ''.join(alpha_dict.get(i, nums_dict.get(i, i)) for i in input)
    return final_output


if __name__ == '__main__':
    special_string = str(input())
    print(special_string_mapping_v1(special_string))
    print()
    print(special_string_mapping_v2(special_string))