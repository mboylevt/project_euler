from core_functions import prime_lib
import time

print('begin')
start = time.process_time()
prime_lib.gen_primes(1000000)
mid = time.process_time()
print('Fast: ' + str(mid - start))
print('mid')
prime_lib.gen_primes_slow(1000000)
end = time.process_time()
print('end')
print('Slow: ' + str(end - mid))
