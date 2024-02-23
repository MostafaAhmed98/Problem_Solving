# n = int(input("Enter Your N: \n"))
# rows = n
#
# start_top = 0
# space_before_astric = n - 1
# astric_count = 1
# while start_top < rows:
#     print(space_before_astric * " ", "*" * astric_count, end="")
#     print()
#     start_top += 1
#     space_before_astric -= 1
#     astric_count += 2
#
# start_bot = 0
# astric_count -= 2
# space_before_astric += 1
# while start_bot < rows:
#     print(space_before_astric * " ", "*" * astric_count, end="")
#     print()
#     start_bot += 1
#     space_before_astric += 1
#     astric_count -= 2

# Solution 2
n = int(input("Enter Your N: \n"))

row = 1

while row <= n:
    start_count = 1
    while start_count <= n - row: # 5 - 1
        print(" ", end="")
        start_count += 1
    start_count = 1
    while start_count <= 2 * row - 1: # (2 * 1) - 1 = 1
        print("*", end="")
        start_count += 1
    print()
    row += 1

row = n

while row > 0:
    start_count = 1
    while start_count <= n - row: # 5 - 1
        print(" ", end="")
        start_count += 1
    start_count = 1
    while start_count <= 2 * row - 1: # (2 * 1) - 1 = 1
        print("*", end="")
        start_count += 1
    print()
    row -= 1