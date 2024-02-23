num = int(input("Enter Your Number: \n"))

# Is even using %2
is_even = (num % 2) == 0

# Is even using /2
is_even_2 = ((num / 2) - (num // 2)) == 0

# Is even using %10
last_digit = num % 10
is_even_3 = last_digit == 0 or last_digit == 2 or last_digit == 4 or last_digit == 6 or last_digit == 8

print(is_even, is_even_2, is_even_3)
