def is_palindrome(word):
    if word == word[-1::-1]:
        return 'Yes'
    return 'No'


if __name__ == "__main__":
    word = str(input())
    print(is_palindrome(word))
