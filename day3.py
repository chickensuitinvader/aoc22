def read(fn):
    with open(fn, 'r') as fp:
        for ln in fp:
            ln = ln.strip()
            yield ln

def read_three(fn):
    i = 0
    lns = []
    for ln in read(fn):
        lns.append(set(ln))
        i += 1
        if i == 3:
            lns_ = lns
            lns = []
            i = 0
            yield lns_

def part_1(fn):
    score = 0
    for ln in read(fn):
        N = len(ln)
        x1, x2 = set(ln[:N//2]), set(ln[N//2:])
        p = x1.intersection(x2)
        z = sum(ord(pi) - 64 for pi in p)
        score += (z + 26) if z < 27 else (z - 32)
    print(score)


def part_2(fn):
    score = 0
    for lns in read_three(fn):
        x1, x2, x3 = lns
        p = x1.intersection(x2).intersection(x3)
        z = sum(ord(pi) - 64 for pi in p)
        score += (z + 26) if z < 27 else (z - 32)
    print(score)


if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1])
    part_2(sys.argv[1])
    print(f"Took {time.perf_counter() - tic} s")