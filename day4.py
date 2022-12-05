def read(fn):
    with open(fn, 'r') as fp:
        for ln in fp:
            ln = ln.strip()
            a, b = ln.split(',')
            a0, a1 = (int(i) for i in a.split('-'))
            b0, b1 = (int(i) for i in b.split('-'))
            yield a0, a1, b0, b1

def part_1(fn):
    score = 0
    for a0, a1, b0, b1 in read(fn):
        if a0 >= b0 and a1 <= b1:
            score += 1
        elif b0 >= a0 and b1 <= a1:
            score += 1 
    print(score)

def part_2(fn):
    score = 0
    for a0, a1, b0, b1 in read(fn):
        if b0 <= a0 <= b1:
            score += 1
        elif a0 <= b0 <= a1:
            score += 1
    print(score)

if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")