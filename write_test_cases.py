test_cases_num = int(input("Enter The Number of test cases: \n"))

while 0 < test_cases_num:
    num_to_be_summed = int(input())
    sum = 0
    num_init = num_to_be_summed
    while num_to_be_summed > 0:
        sum += num_to_be_summed
        num_to_be_summed -= 1
    print(f" Sum From 1 to {num_init} = {sum}")
    test_cases_num -= 1
