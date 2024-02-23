n = int(input("Enter N: \n"))

nums_even_sum = 0
nums_even_count = 0
nums_odd_sum = 0
nums_odd_count = 0

while n > 0:
    num = int(input())
    if n % 2 == 0:
        nums_even_sum += num
        nums_even_count += 1
    else:
        nums_odd_sum += num
        nums_odd_count += 1
    n -= 1
print(nums_even_sum/nums_even_count, " ", nums_odd_sum/nums_odd_count)