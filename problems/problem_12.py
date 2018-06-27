import math

from core_functions import series_generators

tris = series_generators.triangle_numbers()

def count_divisors(num):
    count = 0
    for i in range(1, int(math.sqrt(num)+1)):
        if num % i == 0:
            if number / i == i:
                count += 1
            else:
                count += 2
    return count

while True:
# for i in range(0,100000):
    number = next(tris)
    divisors = count_divisors(number)
    if divisors >= 500:
        print("Number: " + str(number))
        break