from core_functions import series_generators

fib = series_generators.fibonocci()
fib_value = next(fib)
total = 0
while fib_value < 4000000:
    if fib_value % 2 == 0:
        total += fib_value
    fib_value = next(fib)

print(total)