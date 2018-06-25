import math

from core_functions import prime_lib

big_guy = 600851475143
limit = math.floor(math.sqrt(big_guy))

primes = prime_lib.gen_primes(limit=limit)

for prime in primes[::-1]:
    if big_guy % prime == 0:
        print(prime)
        break

