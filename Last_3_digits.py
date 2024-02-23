num = int(input("Enter Your Number: \n"))

# 1458
last_3_digit = num % 1000  # 458
last_digit = last_3_digit % 10  # 8
remove_last_digit = last_3_digit // 10  # 45
sec_digit = remove_last_digit % 10  # 5
remove_last_digit_2 = remove_last_digit // 10  # 4
third_digit = remove_last_digit_2  # 4

print(last_digit + sec_digit + third_digit)
