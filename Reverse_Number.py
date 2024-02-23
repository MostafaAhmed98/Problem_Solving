N = int(input())

number = 0

while N > 0:  # 123, 12, 1
    last_digits = N % 10 # 3, 2, 1
    N //= 10 # 12, 1, 0

    number = number * 10 + last_digits # 3, 32, 321

print(number, number * 3)
