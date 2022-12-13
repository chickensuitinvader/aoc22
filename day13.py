import functools

def read(fn):
    with open(fn, 'r') as fp:
        for ln in fp:
            yield ln.strip()

def read_pairs(fn):
    working = []
    for ln in read(fn):
        ln = ln.strip()
        if ln != '':
            working.append(eval(ln))
        else:
            pair = working
            working = []
            yield pair
    yield working

def clean_read(fn):
    for ln in read(fn):
        if ln != '':
            yield eval(ln)

def compare(x, y):

    for xi, yi in zip(x, y):
        int_x = isinstance(xi, int)
        int_y = isinstance(yi, int)
        if int_x and int_y:
            if xi == yi:
                continue
            return xi - yi
        res = compare([xi] if int_x else xi, [yi] if int_y else yi)
        if res:
            return res
    return len(x) - len(y)


def part_1(fn):
    score = 0

    for i, (x, y) in enumerate(read_pairs(fn)):
        res = compare(x, y)
        if res < 0:
            score += i+1
    print(score)

def part_2(fn):
    to_sort = [*clean_read(fn), [[2]], [[6]]]
    packets = sorted(to_sort, key=functools.cmp_to_key(compare))
    print((packets.index([[2]])+1) * (packets.index([[6]])+1))


if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")