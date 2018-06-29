import math
sum = 0
for i in range(2,1000000):
    number = str(i)
    rolling_sum = 0.0
    for digit in number:
        rolling_sum += int(math.pow(int(digit),5))
    if rolling_sum == i:
        sum+=i
        print(number)

print(sum)