import math
terms = set()
for a in range(2,101):
    for b in range (2,101):
        terms.add(int(math.pow(a,b)))

print(len(terms))