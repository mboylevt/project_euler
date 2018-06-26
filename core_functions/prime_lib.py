import math


def gen_primes_slow(limit=1000000):
    primes = []
    for i in range(2, limit):
        is_prime = True
        for x in range(2, int(math.sqrt(i))):
            if i % x == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes


def gen_primes(limit=1000000):
    sieve = [False] * limit
    primes = []
    for j in range(2, limit):
        if sieve[j]:
            continue
        primes.append(j)
        if j*j > limit:
            continue
        for i in range(j, limit, j):
            sieve[i] = True
    return primes


def gen_primes_generator(start=2, limit=1000000):
    sieve = [False] * (limit+1)
    for j in range(start, limit+1):
        if sieve[j]:
            continue
        yield j
        if j*j > limit:
            continue
        for i in range(j, limit+1, j):
            sieve[i] = True


def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2,x):
            if x % n == 0:
               return False
        return True

def psieve():
    import itertools
    yield from (2, 3, 5, 7)
    D = {}
    ps = psieve()
    next(ps)
    p = next(ps)
    assert p == 3
    psq = p*p
    for i in itertools.count(9, 2):
        if i in D:      # composite
            step = D.pop(i)
        elif i < psq:   # prime
            yield i
            continue
        else:           # composite, = p*p
            assert i == psq
            step = 2*p
            p = next(ps)
            psq = p*p
        i += step
        while i in D:
            i += step
        D[i] = step