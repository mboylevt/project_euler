import time

start = time.time()
is_1000 = []
for a in range(1,998):
    for b in range(1, 998):
        for c in range(1, 998):
            if a+b+c == 1000:
                is_1000.append([a,b,c])
mid = time.time()
print(is_1000)
for [a,b,c] in is_1000:
    if ((a*a)+(b*b)) == (c*c):
        print(str(a*b*c))

end = time.time()

print("3 loop: " + str(mid - start))

print("product: " + str(end - mid))