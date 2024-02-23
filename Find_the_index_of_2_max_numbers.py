def find_two_maximum_numbers(lst):
    """Find the two largest numbers in a list and their respective indices.
        This function takes a list of numbers as input and returns a tuple containing
        the following elements:
        - The largest number in the list.
        - The index of the largest number in the list.
        - The second largest number in the list.
        - The index of the second largest number in the list.
        Args:
            lst (list): A list of numbers.
        Returns:
            tuple: A tuple containing four elements in the order:
                (biggest_number, idx_1, sec_biggest_number, idx_2).
        """
    biggest_number = max(lst)
    idx_1 = lst.index(biggest_number)
    lst[idx_1] = 0
    sec_beggest_number = max(lst)
    idx_2 = lst.index(sec_beggest_number)
    lst[idx_1] = biggest_number
    return biggest_number, idx_1, sec_beggest_number, idx_2


if __name__ == '__main__':
    lst = list(map(int, input().split()))
    num1, idx_1, num2, idx_2 = find_two_maximum_numbers(lst)
    print(f" idx_1 is {idx_1} and its value is {num1}", f"\n idx_2 is {idx_2} and its value is {num2} ")
