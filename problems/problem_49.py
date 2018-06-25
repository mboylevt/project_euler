import bisect
from core_functions import primes

limit = 10000

prime_list = primes.gen_primes(limit)
prime_list = prime_list[bisect.bisect_right(prime_list,1000):]

for i in prime_list:
    for j in prime_list:
        if i == j:
            continue
        k = j + (j-i)
        if k in prime_list:
            if sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
                print(str(i) + ' ' + str(j) + ' ' + str(k))
                print("Difference: " + str(j-i))