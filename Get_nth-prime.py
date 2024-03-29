def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def nth_prime(n):
    prime_number = 1
    for i in range(0, n):
        prime_number += 1
        while not is_prime(prime_number):
            prime_number += 1

    return prime_number


# def nth_prime(n):
#     start = 2
#     while n > 0:
#         if is_prime(start):
#             n -= 1
#             if n == 0:
#                 return start
#         start += 1
#     return -1


print(nth_prime(8))
