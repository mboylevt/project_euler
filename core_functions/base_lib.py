import math


def get_divisors(number):
    divisors = []
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return divisors


def get_sum_of_divisors(number):
    d_sum = 0
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            d_sum += i
    return d_sum

def get_abundant_numbers(limit):
    abundant_numbers = []
    for test_number in range(0,limit+1):
        if get_sum_of_divisors(test_number) > test_number:
            abundant_numbers.append(test_number)
    return abundant_numbers