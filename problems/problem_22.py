names_source = open('../data/p022_names.txt', 'r')
names = sorted(names_source.read().replace('"', '').split(','))
total = 0

for i in range(0,len(names)):
    name = names[i]
    name_sum = 0
    for l in name:
        name_sum += (ord(l) - 64)
    total += name_sum * (i+1)

print(str(total))