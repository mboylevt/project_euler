import math

num = math.factorial(100)
s_num = str(num)
total = 0
for n in s_num:
    total += int(n)

print(str(total))