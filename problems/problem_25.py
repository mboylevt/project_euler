from core_functions import series_generators

fibgen = series_generators.fibonocci()
count = 0
while True:
    fibseq = next(fibgen)
    if len(str(fibseq)) == 1000:
        print(count)
        break
    count += 1