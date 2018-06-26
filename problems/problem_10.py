from core_functions import prime_lib


sieve = prime_lib.psieve()
sum = 0
while True:
    prime = next(sieve)
    if prime > 2000000:
        break
    sum += prime

print(str(sum))