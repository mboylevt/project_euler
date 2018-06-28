from core_functions import base_lib

def get_sum_of_divisors(divisors):
    sum = 0
    for d in divisors:
        sum += d
    return sum

amicable_numbers = set()

for i in range(220,9999):
    divisors_a = base_lib.get_divisors(i)
    sum_a = get_sum_of_divisors(divisors_a)
    divisors_b = base_lib.get_divisors(sum_a)
    sum_b = get_sum_of_divisors(divisors_b)
    if i == sum_a:
        continue
    if i == sum_b:
        amicable_numbers.add(sum_a)
        amicable_numbers.add(sum_b)

print(amicable_numbers)
total = 0
for i in amicable_numbers:
    total += i

print(str(total))