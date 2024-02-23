def conc_strings_v1(str1, str2):
    len_str1, len_str2 = len(str1), len(str2)
    counter = 0
    final_word = ''
    if len_str1 > len_str2:
        counter = len_str1
    else:
        counter = len_str2
    for i in range(counter):
        if i < len_str1:
            final_word += str1[i]
        if i < len_str2:
            final_word += str2[i]
    return final_word


def conc_strings_v2(str1, str2):
    for c1, c2 in zip(str1, str2):
        print(c1 + c2, end="")

    if len(str1) < len(str2):
        str1, str2 = str2, str1

    if len(str1) > len(str2):
        print(str1[len(str2):], end="")
    print()


if __name__ == "__main__":
    word_1, word_2 = input().split()
    conc_strings_v2(word_1, word_2)
