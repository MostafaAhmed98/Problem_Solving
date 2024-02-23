T = int(input())

while T > 0:
    number_of_inputs = int(input())
    start_count = 1
    all_sum = 0
    while start_count <= number_of_inputs:
        number_to_be_sqr = int(input())
        start_count_internal = start_count
        sum_of_sqr_numbers_int = 1
        while start_count_internal > 0:
            sum_of_sqr_numbers_int *= number_to_be_sqr
            start_count_internal -= 1
        all_sum += sum_of_sqr_numbers_int
        start_count += 1
    print(f"Sum is {all_sum}")
    T -= 1


# For Loop Solution
# T = int(input())
#
# for i in range(T):
#     N, all_sum = int(input()), 0
#     for j in range(N):
#         value, result = int(input()), 1
#         for k in range(j + 1):
#             result *= value
#
#         all_sum += result
#     print('Sum is', all_sum)