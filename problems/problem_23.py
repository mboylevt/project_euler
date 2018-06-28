from core_functions import base_lib

upper_limit = 28123

abundant_numbers = base_lib.get_abundant_numbers(upper_limit)

sum_of_abundants = [False] * (upper_limit*2+1)

for i in abundant_numbers:
    for j in abundant_numbers:
            sum_of_abundants[i+j] = True

total_non_abundants = 0
for i in range(0,30000):
    if not sum_of_abundants[i]:
        total_non_abundants+=i

print(str(total_non_abundants))