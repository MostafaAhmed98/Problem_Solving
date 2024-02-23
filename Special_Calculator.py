calc_is_on = True

while calc_is_on:
    print(
        "Menu:\n Enter 1 to sum numbers from 1 to N\n Enter 2 to evaluate simple 2 numbers expressions (e.g. 2 + 3)\n "
        "Enter 3 to end the program")

    user_choice = str(input("Enter Choice from 1 to 3: \t"))
    if user_choice != '1' and user_choice != '2' and user_choice != '3':
        print("Invalid Input ... Try again")
        continue

    # Start of Choice 1
    if user_choice == '1':
        number_of_choice_1 = int(input("Enter a number: \t"))
        # sum_of_number = 0
        # counter = number_of_choice_1 - 1
        # while counter > 0:
        #     sum_of_number += counter
        #     counter -= 1
        sum_of_number = (number_of_choice_1 * (number_of_choice_1 + 1) // 2)
        print(f"Sum from 1 to {number_of_choice_1} is {sum_of_number}")
        continue
    # End of choice 1

    # Start of Choice 2
    elif user_choice == '2':
        num_1_in_choice_2, operator_in_choice_2, num_2_in_choice_2 = map(str,
                                                                         input("Enter a simple expression: \t").split())
        num_1_in_choice_2, num_2_in_choice_2 = int(num_1_in_choice_2), int(num_2_in_choice_2)

        if operator_in_choice_2 == "-":
            result_choice_2 = num_1_in_choice_2 - num_2_in_choice_2
        elif operator_in_choice_2 == "+":
            result_choice_2 = num_1_in_choice_2 + num_2_in_choice_2
        elif operator_in_choice_2 == "*":
            result_choice_2 = num_1_in_choice_2 * num_2_in_choice_2
        elif operator_in_choice_2 == "**":
            result_choice_2 = num_1_in_choice_2 ** num_2_in_choice_2
        elif operator_in_choice_2 == "/":
            result_choice_2 = num_1_in_choice_2 / num_2_in_choice_2
        else:
            print("Sorry: No Way to compute this expression")
            continue
        print(f"Expression Value is {result_choice_2}")
    # End of choice 2

    else:
        break
