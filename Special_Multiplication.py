def special_multiplication(string):
    result = ""
    for idx, char in enumerate(string):
        result += char * (idx + 1)
    print(result)


special_multiplication("abcxf")
