import math


def get_divisors(number):
    divisors = []
    for i in range(1, int(number/2)+1):
        if number % i == 0:
            divisors.append(i)
    return divisors