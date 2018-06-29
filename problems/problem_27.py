from core_functions import prime_lib

max_count = 0
for a in range(-999,1000):
    for b in range(-1000,1000):
        cur_count = n = 0
        while prime_lib.is_prime((n*n) + a*n + b):
            cur_count += 1
            n += 1
        if cur_count > max_count:
            print("New max {}".format(cur_count))
            print("Coefficients: A={}, B={}.  Product = {}".format(a,b,a*b))
            max_count = cur_count