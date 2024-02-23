def our_int(word_to_int):
    res = 0
    digits = '0123456789'
    for char in word_to_int:
        res = res * 10 + digits.find(char)
    return res * 3


if __name__ == "__main__":
    word = str(input())
    print(our_int(word))
