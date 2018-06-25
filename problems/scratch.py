from core_functions import primes
import time

print('begin')
start = time.process_time()
primes.gen_primes(1000000)
mid = time.process_time()
print('Fast: ' + str(mid - start))
print('mid')
primes.gen_primes_slow(1000000)
end = time.process_time()
print('end')
print('Slow: ' + str(end - mid))
