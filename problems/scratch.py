from core_functions import prime_lib
import time

sieve = prime_lib.psieve()

for i in range (0,10):
    print(next(sieve))