def letters_frequency_v1(letters):
    lower_string = letters.lower()
    out_dict = {}
    for i in lower_string:
        if i in out_dict:
            out_dict[i] += 1
        else:
            out_dict[i] = 1
    for key, value in sorted(out_dict.items()):
        print(f"Letter {key} repeated {value} times")


def letters_frequency_v2(letters):
    out_dict = {}
    for char in letters:
        char = char.lower()
        out_dict.setdefault(char, 0)
        out_dict[char] += 1
    for key in sorted(out_dict):
        print(f"Letter {key} repeated {out_dict[key]} times")


if __name__ == '__main__':
    letters = str(input())
    letters_frequency_v1(letters)
    print()
    letters_frequency_v2(letters)
