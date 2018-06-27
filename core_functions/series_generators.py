def fibonocci():
    a = 0
    b = 1
    while True:
        yield a
        a, b = b, a + b


def triangle_numbers():
    a = 1
    count = 1
    while True:
        yield a
        count += 1
        a += count


def pascals_triangle():
    yield from ([1], [1,1])
    row = [1,1]
    while True:
        new_row = [0] * (len(row) + 1)
        for index in range(0,len(new_row)):
            if index == 0 or index == len(row):
                new_row[index] = 1
            else:
                new_row[index] = row[index] + row[index-1]
        row = new_row
        yield row
