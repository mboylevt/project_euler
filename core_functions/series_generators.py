

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