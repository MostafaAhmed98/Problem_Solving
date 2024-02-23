def grouping(string):
    final_out = string[0:1]
    for i in range(1, len(string)):
        if string.lower()[i] == string.lower()[i - 1]:
            final_out = final_out + string[i]
        else:
            final_out = final_out + ',' + string[i]
    return final_out


if __name__ == "__main__":
    word = input()
    print(grouping(word))
