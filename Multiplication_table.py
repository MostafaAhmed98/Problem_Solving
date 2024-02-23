N, M = map(int, input().split())

start_n = 1

while start_n <= N:
    start_m = 1
    while start_m <= M:
        print(f"{start_n} x {start_m} = {start_n * start_m}")
        start_m += 1
    start_n += 1
