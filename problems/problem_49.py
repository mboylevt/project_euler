from core_functions import primes

start = 1000
limit = 10000

prime_list = primes.gen_primes(start, limit)

for i in prime_list:
    for j in prime_list:
        if i == j:
            continue
        k = j + (j-i)
        if k in prime_list:
            if sorted(str(i)) == sorted(str(j)) == sorted(str(k)):
                print(str(i) + ' ' + str(j) + ' ' + str(k))
                print("Difference: " + str(j-i))