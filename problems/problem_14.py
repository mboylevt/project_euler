def sequence_generator():
    start = yield
    val = start
    while True:
        if val % 2 == 0:
            val = val/2
            yield val
        else:
            val = (3 * val) + 1
            yield val

max = 0
for i in range(2,1000000):
    # print("Testing {}".format(i))
    count = 2
    gen = sequence_generator()
    next(gen)
    gen.send(i)
    val = next(gen)
    while val != 1:
        val = next(gen)
        count += 1
    if count > max:
        max = count
        print("New max: {} generates length {}".format(i,max))

print("Max: {}".format(max))