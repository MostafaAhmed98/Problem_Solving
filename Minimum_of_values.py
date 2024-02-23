T = int(input("Enter Your T: \n"))

while T > 0:
    N = int(input("Enter Your N: \t"))
    min = 10**9
    while N > 0:
        num = int(input())
        if num < min:
            min = num
        N -=1
    print(f"Min Value is: {min}")
    T -= 1
