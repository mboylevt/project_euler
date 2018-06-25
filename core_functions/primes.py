import math

def gen_primes(start, limit):
    primes = []
    for i in range(start, limit):
        is_prime = True
        for x in range(2, int(math.sqrt(i))):
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes