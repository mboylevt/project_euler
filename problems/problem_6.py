import math

sum_of_squares = 0
sum = 0
for i in range(1,101):
    sum += i
    sum_of_squares+=(i*i)

square_of_sums = sum*sum
difference = square_of_sums - sum_of_squares
print(difference)