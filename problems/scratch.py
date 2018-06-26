from core_functions import prime_lib
import time

i = '0123443210'
length = len(i)
first_half = i[:int(length/2)]
second_half = i[int(length / 2):]
print(first_half)
print(second_half[::-1])

if first_half == second_half[::-1]:
    print("match!")