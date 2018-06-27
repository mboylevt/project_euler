from core_functions import prime_lib, series_generators
import time

sieve = prime_lib.psieve()

pascal = series_generators.pascals_triangle()

for i in range (1,100):
    print(str(next(pascal)))