n = int(input("Enter N: \n"))

while n >= 0:
    start = 1
    while start <= n:
        print("*", end='')
        start += 1
    print()
    n -= 1
