num = int(input("Enter Your Number: \n"))

check = num > 1000
last_4_digits = (check * num) % 10000
fourth_digit = last_4_digits // 1000

print(fourth_digit)

# Solution 2

# num_without_last_3_digits = num // 1000
# print(num_without_last_3_digits % 10)
