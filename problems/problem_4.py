limit = 999

palindromes = []
for i in range(100,999):
    for j in range(100,999):
        sum = str(i * j)
        length = len(sum)
        if length % 2 != 0:
            continue
        first_half = sum[:int(length/2)]
        second_half = sum[int(length / 2):]
        if first_half == second_half[::-1]:
            palindromes.append(i*j)

print(sorted(palindromes,reverse=True))