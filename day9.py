dirx = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}

pos = {
    True: 1,
    False: -1,
}

def read(fn):
    with open(fn, 'r') as fp:
        for ln in fp:
            d, n = ln.strip().split(' ')
            # print(ln.strip())
            yield (dirx[d], int(n))

def visualise(ht, v):
    sz = [[*[hi[0] for hi in ht], *(vi[0] for vi in v)], [*[hi[1] for hi in ht], *(vi[1] for vi in v)]]
    N = (max(sz[0]) - min(min(sz[0]), 0) + 1, max(sz[1]) - min(min(sz[1]), 0) + 1)
    arr = [['.']*N[1] for _ in range(N[0])]
    for vi in v:
        arr[vi[0]][vi[1]] = '#'
    for i, x in reversed(list(enumerate(ht))):
        arr[x[0]][x[1]] = str(i)
    for z in reversed(list(zip(*arr))):
        print(''.join(z))
    print(flush=True)

def part_1(fn, viz=False):
    h = [0, 0]
    t = [0, 0]
    v = {tuple(t)}
    for d, n in read(fn):
        for _ in range(n):
            h[0] += d[0]
            h[1] += d[1]

            dx = h[0] - t[0]
            dy = h[1] - t[1]

            if abs(dx) == 2 or abs(dy) == 2:
                t[0] += update(dx)
                t[1] += update(dy)
                v.add(tuple(t))
        if viz:
            visualise([h, t], v)

    print(len(v))

def update(d):
    if d == 0:
        return 0
    return pos[d > 0]

_K = 10
def part_2(fn, viz=False):
    ks = [[0, 0] for _ in range(_K)]
    v = {tuple(ks[-1])}
    for d, n in read(fn):
        for _ in range(n):
            ks[0][0] += d[0]
            ks[0][1] += d[1]

            for hi, ti in zip(range(0, _K-1), range(1, _K)):
                h = ks[hi]
                t = ks[ti]
                dx = h[0] - t[0]
                dy = h[1] - t[1]

                if abs(dx) == 2 or abs(dy) == 2:
                    t[0] += update(dx)
                    t[1] += update(dy)

                    v.add(tuple(ks[-1]))
        if viz:
            visualise(ks, v)

    print(len(v))


if __name__ == "__main__":
    import sys
    import time
    tic = time.perf_counter()
    part_1(sys.argv[1], sys.argv[2:3] or False)
    part_2(sys.argv[1], sys.argv[2:3] or False)
    print(f"Took {time.perf_counter() - tic} s")